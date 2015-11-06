The Bazaar Package Importer
###########################

:date: 2010-03-14 18:55
:slug: ubuntu/16-bazaar-packge-importer

The Bazaar package importer is a service that we run to allow people to use
Bazaar for Ubuntu development by importing any source package uploads in to
bzr. It's not something that most Ubuntu developers will interact with directly,
but is of increasing importance.

I've spent a lot of time working in the background on this project, and while
the details have never been secret, and in fact the code has been available
for a while, I'm sure most people don't know what goes on. I wanted to rectify
that, and so started with some `wiki documentation`_ on the internals. This post
is more abstract, talking about the archtecture.

While it has a common pattern of requirements, and so those familiar with
the architecture of job systems will recognise the solution, the devil is in the
details. I therefore present this as a case-study of one such system that can
be used to constrast other similar sytstems as an aid to learning how differing
requirements affect the finished product.

.. _wiki documentation: https://wiki.ubuntu.com/DistributedDevelopment/UnderTheHood

The Problem
-----------

For the `Ubuntu Distributed Development initative`_ we have a need for a
process that imports packages in to bzr on an ongoing basis as they are
uploaded to Ubuntu. This is so that we can have a smooth transition rather
than a flag day where everyone switches. For those that are familiar with
them think Launchpad's code imports but with Debian/Ubuntu packages as the
source, rather than a foreign VCS.

.. _Ubuntu Distributed Development initative: https://wiki.ubuntu.com/DistributedDevelopment

This process is required to watch for uploads to Debian and Ubuntu and trigger
a run to import that upload to the bzr branches, pushing the result to LP. It
should be fast, though we currently have a publication delay in Ubuntu that
means we are used to latencies of an hour, so it doesn't have to be greased
lightning to get acceptance. It is more important to be reliable, so that the
bzr branches can be assumed to be up to date, that is crucial for acceptance.

It should also keep an audit trail of what it thinks is in the branches. As
we open up write access to the resulting branches to Ubuntu developers we can
not rely on the content of the branches not being tampered with. I don't expect
this will ever be a problem, but I wanted to ensure that we could at least detect
tampering, even if we couldn't know exactly what had happened by keeping private
copies of everything.

The Building Blocks
-------------------

The first building block of the solution is the import script for a single package.
You can run this at any time and it will figure out what is unimported, and do
the import of the rest, so you can trigger it as many times as you like without
worrying that it will cause problems. Therefore the requirement is only to trigger
it at least once when there has been an upload since the last time it was run, which
is a nicer requirement than "exactly once per upload" or similar.

However, as it may import to a number of branches (both lucid and karmic-security
in the case of a security upload, say), and these must be consistent on Launchpad,
only one instance can run at once. There is no way to do atomic operations on sets
of branches on Launchpad, therefore we use locks to ensure that only one process
is running per-package at any one time. I would like to explore ways to remove this
requirement, such as avoiding race conditions by operating on the Launchpad branches
in a consistent manner, as this would give more freedom to scale out.

The other part of the system is a driver process. We use separate processes so that
any faults in the import script can be caught in the supervisor process, with the
errors being logged. The driver process picks a package to import and triggers a run
of the script for it. It uses something like the following to do that::

    write_failure(package, "died")
    try:
        import(package)
    except:
        write_failure(packge, stderr)
    finally:
        remove_failure(package)

write_failure creates a record that the package failed to import with a reason. This
provides a list of problems to work through, and also means that we can avoid trying
to import a package if we know it has failed. This ensures that previous failures are
dealt with properly without giving them a chance to corrupt things later.

Queuing
-------

I said that the driver picks a package and imports it. To do this it simply queries
the database for the highest priority job waiting, dispatching the result, or
sleeping if there are no waiting jobs. It can actually dispatch multiple jobs in
parallel as it uses processes to do the work.

The queue is filled by a couple of other processes triggered by cron. This is useful
as it means that further threads are not required, and there is less code running
in the monitor process, and so less chance that bugs will bring it down.

The first process is one that checks for new uploads since the last check and adds a
job for them, see below for the details. The second is one that looks at the current
list of failures and retries some of them automatically, if the failure looks like it
was likely to be transient, such as a timeout error trying to reach Launchpad. It
only retries after a timeout of a couple of hours has elapsed, and also if that package
hasn't failed in that same way several times in a row (to protect against e.g. the data
that job is sending to LP causing it to crash and so give timeout errors.)

It may be better to use an AMQP broker or a job server such as Gearman for this task,
rather that just using the database. However, we don't really need any of the more
advanced features that these provide, and already have some degree of loose-coupling,
so using fewer moving parts seems sensible.

Reacting to new uploads
-----------------------

I find this to be a rather neat solution, thanks to the Launchpad team. We use
the API for this, notably a method on IArchive called getPublishedSources().
They key here is the parameter "created_since_date". We keep track of this and
pass it to the API calls to get the uploads since the last time we ran, and
then act on those. Once we processed them all then we update the stored
date and go around again.

This has some nice properties, it is a poll interface, but has some things in
common with an event-based one. Key in my eyes is that we don't have to have
perfect uptime in order to ensure we never miss events.

However, I am not convinced that we will never get a publication that appears
later than one that we have dealt with, but that reports an earlier time.
If this happens we would never see it. The times we use always come from
LP, so don't require synchronised clocks between the machine where this
runs and the LP machines, but it could still happen inside LP.
To avoid this I subtract a delta when I send the request, so assuming
the skew would not be greater than that delta we won't get hit. This does
mean that you repeatedly try and import the same things, but that
is just a mild inefficiency.

Synchronisation
---------------

There is a synchronisation point when we push to Launchpad. Before and after
this critical period we can blow away what we are doing with no issues. During
it though we will have an inconsistent state of the world if we did that.
Therefore I used a protocol to ensure that we guard this section.

As we know locking ensures that only one process runs at a time, meaning that
the only way to race is with "yourself." All the code is written to assume
that things can go down at any time as I said, the supervisor catches this
and marks the failures, and even guards against itself dying. Therefore
when it picks back up and restarts the jobs that it was processing before
dying it needs to ensure that it wasn't in the critical section.

To do this we use a three-phase commit on the audit data to accomany the push.
When we are doing the import we track the additions to the audit data separately
from the committed data. Then if we die before we reach the critical section
we can just drop it again, returning to the inital state.

The next phase marks in the database that the critical section has begun. We then
start the push back. If we die here we know we were in the critical section and can
restart the push. Only once the push has fully completed do we move the new audit
data in to place.

The next step cleans up the local branches, dying here means we can just carry
on with the cleanup. Finally the mark that we are in the critical section is
removed, and we are back to the start state, indicating that the last run was
clean, and any subsequent run can proceed.

All of this means that if the processes go down for any reason, they will clean
up or continue as they restart as normal.

Dealing with Launchpad API issues
---------------------------------

The biggest area of operational headaches I have tends to come from using the
Launchpad API. Overall the API is great to have, and generally a pleasure to
use, but I find that it isn't as robust as I would like. I have spent quite
some time trying to deal with that, and I would like to share some tips from
my experience. I'm also keen to help diagnose the issues further if any Launchpad
developers would like so that it can be more robust off the bat.

The first tip is: partition the data. Large datasets combined with fluctuating
load may mean that you suddenly hit a timeout error. Some calls allow you to
partition the data that you request. For instance, getPublishedSources that
I spoke about above allows you to specify a distro_series parameter. Doing

::

      distro.main_archive.getPublishedSources()

is far far more likely to timeout than

::

     for s in distro.series:
         distro.main_archive.getPublishedSources(distro_series=s)

in fact, for Ubuntu, the former is guaranteed to timeout, it is a lot of data.

This is more coding, and not the natural way to do it, therefore it would be
great if launchpadlib automatically partioned and recombined the data.

The second tip is: expect failure. This one should be obvious, but the API doesn't
make it clear, unlike something like python-couchdb. It is a webservice, so you
will sometimes get HTTP exceptions, such as when LP goes offline for a rollout.
I've implemented randomized exponential backoff to help with this, as I tend
to get frequent errors that don't apparently correspond to service issues.
I very frequently see 502 return codes, on both edge and production, which I believe
means that apache can't reach the appservers in time.

Summary
-------

Overall, I think this architecture is good, given the synchronisation requirements
we have for pushing to LP, without those it could be more loosely coupled.

The amount of day-to-day hand-holding required has reduced as I have learnt about
the types of issues that are encountered and changed the code to recognise and act
on them.
