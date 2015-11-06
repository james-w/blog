REVU
#parser reST

Quality of packages not in Debian
---------------------------------

While Ubuntu takes most of its packages from Debian, it does contain a few
that are not in Debian, for one reason or another. One common reason is
simply that someone wanted a package that wasn't in Debian, and packaged
it and requested its inclusion.

The fact that these packages are not in Debian means that they are slightly
different to the rest of the packages in Ubuntu, as they are completely
Ubuntu's responsibility to maintain. By including them we are making a
different sort of contract with our users and the authors of the software.

I was interested in how well we do at keeping this contract. A quick bit
of scripting and I found some basic numbers on this. There are 886 packages
in Ubuntu's universe component that are not in Debian. One possible measure
of quality is the number of open bugs against these packages, which is
shown in the following table as frequency counts.

========================== ==================
Number of open bug reports Number of packages
========================== ==================
0                          595
1                          146
2                          49
3                          23
4                          17
5                          14
6                          8
7                          4
8                          3
9                          6
10                         5
11                         4
12                         1
13                         2
15                         2
17                         1
21                         2
22                         1
26                         1
30                         1
82                         1
========================== ==================

So there are few open bugs on these packages, and around two-thirds have
none. However, there are more than 200 open bugs in total, which we would
want to do something about.

To look at how well these bugs are being triaged I looked more closely at
those packages with open bugs, and looked at what percentage of those bugs
were still in the "New" status with an "Undecided" priority, i.e. completely

======================================= ==================
Percent of open bugs untriaged, at most Number of packages
======================================= ==================
20                                      107
40                                      35
60                                      37
80                                      21
100                                     91
======================================= ==================

So again, this isn't too bad, with many packages with less than 5% completely
untriaged bugs. Again though, the numbers are too high, and as this only counts
those bugs that are completely untriaged, I'm sure that most are not triaged to
the level that we would want.

Lastly I wanted to see how much visibility we have in to problems these packages
may have. For this I looked at the number of bug subscribers for the source
package. While this is certainly not everything, I would certainly fell better
if we had one or two people subscribed to the bugs for every one of these
packages.

=========== ==================
Subscribers Number of packages
=========== ==================
0           596
1           232
2           42
3           7
4           6
5           3
=========== ==================

This shows that two thirds of the packages don't have anyone subscribed to the
bugs for these packages.

What about keeping up with upstream? Shipping old versions of packages means they
are likely to be more buggy, and won't be popular with the authors of the software.
The `Ubuntu External Health Status`_ site attempts to track this using the
``debian/watch`` files in the source packages. I attempted to pull the information
about these packages from there.

.. _Ubuntu External Health Status: http://qa.ubuntuwire.com/uehs/

A bit of explanation is in order for those not intimately familiar with Debian
packaging. The ``debian/watch`` file specifies the location of the upstream
source in such a way that new versions can be checked for, and the update of
the package be done semi-automatically. This can't be automated for a package
that has no watch file, so I list the number of those. Also those packages
that have a watch file, but it doesn't work for some reason are listed, as
the watch file is not usable for this, though sometimes that is a transient
problem.

The figures for the number of packages in each of the three states are:

================= ===
Out of date       46
No watch file     495
Broken watch file 32
================= ===

The number of packages that are out of date is not that bad, especially considering
we've been frozen for the last few months. However, there is a large number of
packages without a watch file. This means that there's no automated way to find
out about new versions of the package being released. It's possible to do without
that, but I doubt that all 495 packages have someone watching over them.

Conclusion
~~~~~~~~~~

This is in no way scientific, and I'm very clearly adding some of my bias in to
interpreting the results, but here are my conclusions from the investigation.

The packages that we have in Ubuntu universe but not Debian don't have too many
bugs, but the ones that they do have are under-triaged, and we aren't that aware
of what bugs we have.

Also, we could do more to allow our automated tools for finding out about new
upstream releases work better, again making sure we are aware when a package
is out of date.

Actions
~~~~~~~

1. Firstly, I am going to discuss with the QA team ways in which we can improve the
   QA on these packages. I will add an item to the QA team's agenda for the next
   meeting that I am able to attend to do this. A couple of ideas I have are:

     * a hug day to triage the bugs currently open on these packages.
     * a team that is subscribed to all packages not in Debian. I would like to
       discuss making this the MOTU team so that all reports end up on the
       mailing list, but that would require more discussion.

1. Secondly, we should improve the situation with the watch files. I will add the
   UEHS page with the list of packages without a watch file to a wiki page of
   easy tasks for people to work on, or perhaps as a harvest data source. The
   UEHS page also lists packages maintained by the Debian QA team on that page,
   and while it would be good to fix those in Debian, it may be a good idea to
   split the lists, not least because the Debian QA team may not appreciate an
   un-coordinated flood of watch files. I will talk to the maintainers of UEHS
   about the feasibility of doing this.

Why Ubuntu?
-----------

The reason we allow packages directly in to Ubuntu is that it brings benefit
to our users. Most packages that enter Ubuntu will be of benefit to someone,
and that's one of our aims, to give our users a good experience, isn't it?
To give our users a good experience we also want high quality though. So we
have a balancing act, splitting our workload between fixing what we have
and spending time bringing in and maintaining new packages.

I would argue that we want to limit the flow of new packages quite severely,
as we are not exactly short of work with our current set of packages.
However, the argument isn't quite as simple as that.

A common way for people to get involved with development is to package
something new and get it uploaded, and later branch out in to working
on existing packages. This means that bringing in lots of new packages
may lead to an influx of new contributors that more than makes up for
the new workload. I'm not sure how strong this link will be, and whether
the ratios will be such that there is a net gain in developer time.

Actions
~~~~~~~

1. Discuss whether the rate of new developers coming from getting a new
   package in to Ubuntu is high enough to warrant the activity.

1. I would also like to discuss ways to encourage people to start their
   involvement by working on existing packages instead.

Why not Debian?
---------------

So, some people will be wondering why all these packages aren't in Debian.
The overarching reason for this is that contributors would rather get their
packages directly in to Ubuntu.

There are several possible reasons for this, and I have heard most of these
stated by someone trying to get their package in to Ubuntu.

One is a simple one, they don't run Debian, and so it's difficult to test
in that environment. Yes, it's not impossible, but it is more work.

There is also a perception among many contributors that getting your package
in to Debian is hard work, with long delays trying to find a sponsor. That's
not something that most of us can really do much about. We can try and tackle
the perception, but without upload right we can't really fix the problem.
There was the `utnubu`_ team that tried to streamline this process, but that is
now defunct as far as I know.

.. _utnubu: http://wiki.debian.org/Utnubu

Another reason is that they may not wish to do this is that they use Ubuntu
and don't really care enough about Debian to do the extra work. This is
something we can try and do something about, explaining the virtues of
getting the package in to Debian, more than just it being the right thing
to do in most cases.

As a counterpoint to this, if the package is going to be useful to a lot
of people then even if the person proposing it for Ubuntu does not want
to try and get it in to Debian then there is likely to be someone
with the interest and skills to maintain it in Debian. For me this means
that the packages that we want to be pulling in to Ubuntu should be
easy to find Debian maintainers for anyway.

Actions
~~~~~~~

1. To tackle the first issue we could have documentation of the best way to
   run Debian to test your packages, and links to the important places to
   keep an eye on the status of your package in Debian. While not solving the
   problem it may convince some to do the extra work as they don't have to
   learn a second way of doing things.

1. For the second issue it would be great to get the utnubu team going again,
   but I can't start this, as I am not a DD.

1. The third issue could again be tackled with documentation, we could have
   a wiki page explaining some of the virtues, and link this from places like
   REVU.

1. Discuss requiring people proposing packages for Ubuntu to at least file
   a request for packaging bug in Debian. This will give a much better chance
   that those interested in packaging for Debian are aware of the existence
   of the package. There are a lot of people interested in packaging for
   Debian that are just looking for something to work on.

REVU and queues
---------------

Now, I want to talk a little bit about REVU, and dealing with queues.

Again, a quick bit of background for those not involved in Ubuntu development.
`REVU`_ is the tool we generally use in Ubuntu to review new packages. Anyone
can propose a package for inclusion in to Ubuntu simply by uploading it there.
Developers can then review it and provide feedback, asking for things to be
changed where necessary. Once it is to a satisfactory standard and has the
support of two people with upload privileges it is uploaded to the archive.

.. _REVU: http://revu.ubuntuwire.com/

REVU is generally a nice platform for doing this work, and I'm not necessarily
criticising its design here, I would just like to examine some of the effects
of some design decisions.

REVU works with three queues. The first is the queue for packages that have
one advocation from an Ubuntu developer. This queue is normally very short
and fast moving, as the package is in good shape and just needs
double-checking. The second queue is all of the packages waiting for a
review. The third queue is for packages that need some work done on them
before they can be uploaded. This means that for developers there is
primarily one queue that contains things they can look at.

This is similar to the sponsorship queue, which is used in Ubuntu as a way
for people without upload rights to make a change to a package in the archive.
This can be seen as just one queue where the developer looks for things
to review and upload.

The sponsorship queue is for changes to packages we already have in the archive,
and we generally want to upload everything on the list, even if not at a
certain point in the development cycle. The difference is that it's generally
easier to give a reason for saying "no" for the rare times that it happens.
This changes the complexion of what it means to keep the queue small.

If an item on the sponsorship queue is incomplete and the person who submitted
it doesn't follow through then we should be picking up the item and ensuring
the problem is fixed. If a package on REVU is incomplete and the person
who submitted it doesn't follow through then there is no real problem. If
the package is popular someone else will eventually pick it up and do the
work.

We don't have (or at least haven't had) the time to review enough packages
on REVU, so the queue is pretty long. Assuming that doesn't change keeping
the queue small will mean removing things because of lack of interest from
the person submitting them. We can work to review more things, but unless
we reach the point where we are accepting more packages than are being
proposed that will always be the case.

There was recently a proposal to help clear the queue of things where the
submitter has given up, so that effort can be focused on the packages where
problems are likely to be fixed. While doing this is makes best use of
developer time I feel that if we feel the need to do this then we have already
lost.

If that is the case then there is a worrying aspect to it. We have had a
bunch of people show an interest in Ubuntu development, and take the first
steps towards becoming a developer, only to get discouraged and give up.

I have heard complaints about it being difficult to find a reviewer, and
I'm sure the people that gave up would not speak fondly of the experience.
However, this hasn't become widespread enough that it has stopped people
giving it a go, and it would be terrible if it did, as having that reputation
may cause potential contributors to look elsewhere.

I think this indicates that we should reconsider the way REVU is presented
within our community. We are presenting a great service to people who are
getting started with packaging and pointing them there saying, put your
package here, "we will review it and you will get it in to Ubuntu." However,
this unfortunately doesn't happen all that often. We are channeling potential
new developers there, knowing that there is a high chance of them getting
discouraged and giving up. On top of that we give the reason that many of
them do give up as one reason that we're not better at reviewing the
packages in the first place.

To me this almost feels like we are trying to put people off from getting
started with Ubuntu development.

It looks as though the proposal to help clear the queue for the start of
this cycle is going to go ahead. That's fine with me, we might as well
make the most of a bad situation and help the reviewers this cycle. If
we are in a position where we feel we need to do the same at the start
of next cycle then I would say that it is clear we have not fixed the
underlying issues, and we really need to stop and reconsider how we
present REVU. 

There is also a slim possibility that the clearing of the queue may
have a different effect. If some contributors are put of by the number
of packages waiting for review, then clearing that may cause them to
put their own up there. While this could imply more potential developers,
it would also mean more packages to review, making it harder to keep
up.

If we keep up this cycle and have a good process going in six months time
then I will be happy, but it will make the rest of this post pretty much
obsolete. I think now is a reasonable time to discuss the "what if?" though.

Changing things
---------------

If we are in the same situation in six months then I think it will
demonstrate that even with a clean slate and a will to fix the problem
we were not able to do enough reviews to keep up with the supply. In that
case we will need to look for ways to turn down the taps, to reduce the
supply.

In no way do I want to send the message that we shouldn't be welcoming
to new contributors, I would just want to explore ways to get them
started with working on our existing packages. It may involve making
it harder to get a package in to Ubuntu though. We may just have
to live with that.

In my opinion there would be two ways to target this, and the solution
may come from some combination of the two. The first would be to make
working on existing packages more attractive, easier to start with,
and the default choice. The second would be to make proposing a new
package more difficult, less attractive, or at least not demoralising
if your package isn't reviewed.

If I had any bright ideas for the first then I would already be trying
to implement them, so let's focus on ways to do the second. Keep thinking
about the first though, and feel free to discuss any ideas with me.

I'll take three ideas from the recent mailing list thread and one I
just had and look at what effects they may have.

Restricting access to REVU
~~~~~~~~~~~~~~~~~~~~~~~~~~

Michael Casadevall proposed restricting those who could upload to REVU.
In particular he proposed restricting it to the "Ubuntu Universe
Contributors" team. These are people that have been given Ubuntu membership
in recognition of their contribution to Ubuntu development. This includes
all Ubuntu developers, but also others who haven't been given upload
rights yet.

This would restrict REVU to those who have contributed to Ubuntu development
in other ways, and so would make it clear that to get started you should
work on existing packages.

In my opinion it also helps with the QA issue, as these people have shown
sustained contribution, and are not going to disappear as soon as the
package is uploaded. When looking for packages on REVU I first look for
names that I know partly for this reason.

As a concession to those that haven't yet reached this stage but want to
get a package in for some reason we could have a kind of sponsorship
process where a member of the team can put a package there for someone
who isn't if they think it is worthy. (While the normal sign and upload
process would work I imagine we would only want to do this at most once,
with the person that proposed the package being able to upload that one
to make changes according to feedback.)

Asking for a rationale
~~~~~~~~~~~~~~~~~~~~~~

REVU could grow a field for the person that proposed the package to
give their reasons why they think the package should be included in
Ubuntu.

While it is currently feasible to reject a package from REVU because it
is not deemed worthwhile I'm not sure that it ever happens. In my opinion
we could use this field as a basis for doing so, perhaps allowing the
proposer to counter and give more reasons.

A more subtle effect I believe it would have would be to make the proposer
think about these issues. There could even be several fields asking about
various different things, such as responsiveness of upstream, potential
number of users, etc. While it probably wouldn't stop anyone from uploading
we could change the REVU help pages to explain that we upload packages
based on their merit, and so if their package is not reviewed they may
understand.

A related idea was to link the packages to brainstorm, so that we could
gauge user interest.

Making REVU per-cycle
~~~~~~~~~~~~~~~~~~~~~

My second proposal was to make REVU per-cycle. This would mean that you
don't propose a package for inclusion in to Ubuntu, but for inclusion
in to the next release. REVU would open the day after a release with
a clean slate, and then close sometime around Feature Freeze, with
packages that were still on there being archived with a message that
they were not successful this time.

I imagine that this would actually include the rationale field, asking
why it should be included this cycle.

This goes further than the previous proposal though, in that it ensures
a clean slate to work from.

More importantly in my opinion is that it focuses on the rationale even
more in my opinion. It asks the question, "For the next release, would
you rather we spent time reviewing this package, or fixing those annoying
bugs that you hit?"

However, I'm not sure that this proposal does enough to encourage people
to work on existing packages to counteract its harshness.

Order packages by uploads
~~~~~~~~~~~~~~~~~~~~~~~~~

We could change the ordering of the packages from chronological order to
ordering by the number of uploads to Ubuntu done by the submitter. We
would then work top down on that list (obviously being able to pick
packages from anywhere if we like).

This would draw an obvious link, upload a bug fix, get more chance of
a review, but do so in a more subtle way, and not penalise brand-new
contributors too much (there are plenty of bite-size tasks that are easy
if you're able to create a package from scratch).

This wouldn't work that well if there was little distribution in the
number of uploads, or the top of the list wasn't reviewed very often,
but it could be a good way to work.

We could obviously substitute number of uploads for something else,
for instance launchpad karma, or mix the numbers somehow. This would
mean that the link was less direct, but it would reward the fantastic
triagers, translators, etc. that want to get in to packaging.

Conclusion
----------

I don't really have a conclusion, but I have plenty to think about,
and I hope you have too. I'll be more than happy to discuss these
issues at any time, so just give me a shout.

