Fixing an Ubuntu bug with Bazaar
################################

:date: 2009-01-22 17:34
:slug: ubuntu/07-fixing-an-ubuntu-bug-with-bazaar

Yesterday as part of `Ubuntu Developer Week`_ I gave a session entitled
"Bazaar for Packaging". At the last minute I decided to change the session
somewhat, so that it would show how things would work if you were to use
bzr to modify an Ubuntu package once Distributed Development is fully up
and running.

.. _Ubuntu Developer Week: https://wiki.ubuntu.com/UbuntuDeveloperWeek

The session went ok, and while I was showing some fairly experimental things
it all worked quite well. The biggest problem was when we grabbed a change
from SVN using the bzr-svn plugin. The rather simple step of extracting a patch
took up quite a lot of the session as bzr-svn initialised it's metatdata about
the Subversion branch. bzr-svn is amazing, it allows you to store a bzr branch
inside an svn repository, while still making it readable to svn. However, to
do this it has to do some fairly intensive transformations to maintain the
mapping. The biggest impact of this is when you access the SVN repository
for the first time though, so it wasn't the smartest idea for an IRC tutorial.
That's the problem with changing your session 10 minutes before it starts.

You can go and read the transcript of the session if you want to see how
all of this worked. I'd like to skip ahead a little bit and show you how
it will work in a short while when launchpad hosts the branches and all
the bits are in place.

First we need to grab the source for the package we want to work on. We'll
grab a whole branch here, but you could just as well use a lightweight
checkout or a stacked branch to transfer less data.

::

  $ bzr branch lp:ubuntu/jaunty/gnome-utils gnome-utils.jaunty

Will give us a local copy of that branch in ``gnome-utils.jaunty``. We can
now make our changes in that branch.

::

  $ cd gnome-utils.jaunty

You can run ``bzr log`` (or better ``bzr viz`` from bzr-gtk or ``bzr qlog`` from
qbzr) to see the history if that is interesting for the change we are making.

We're just going to apply the patch from SVN though. This is what we did in
the session:

::

  $ bzr diff -c svn:8378 http://svn.gnome.org/svn/gnome-utils/trunk | bzr patch

(where bzr patch is supplied by bzrtools. Try it it's cool, it works over any
transport, so you can apply a remote patch file without downloading it)

What we are doing here is in fact a "cherry-pick". bzr will happily do these
for you, but it does the equivalent of diff + patch, it is hoped to improve
this and record which revisions were merged, and use that information to
help you understand what changes have and haven't been merged.

To more directly do a cherry-pick you can run

::

  $ bzr merge -c svn:8378 http://svn.gnome.org/svn/gnome-utils/trunk

(merge the changes introduced in svn revision 8378 of this branch please,
the ``svn:`` is neccesary as bzr and svn count their revisions differently)

However, this won't currently work, as the branches have what is called
"different rich-root support", so we have to use the explicit "diff and
patch" for now. This is a pain, and will hopefully go away sometime soon.
This method would work fine with most bzr branches though.

Once we have applied the patch we write the changelog entry for it. We run
"dch -i -D UNRELEASED", which will create us a new changelog entry, and mark
it as "UNRELEASED" so that it is clear it still needs to be uploaded. Obviously
if there is an existing UNRELEASED changelog entry then we want to add to that.
I would like to write a wrapper than did the right thing here.

For that changelog entry we write the usual thing, something like:

::

  * Don't crash when asked to show a path that has been excluded. (LP: #301952)

Now we are ready to build and test our changes. Running

::

  $ bzr builddeb -S

will spit out a source package in the parent directory, in the same way as
``debuild -S``. We can then build this package in our normal fashion, in
``pbuilder`` say, or upload it to a PPA.

Once we are happy then we can commit our changes. The easiest way to do this
is to run

::

  $ debcommit

which uses our changelog entry as the commit message, saving us from typing
the same thing again.

There's one extra bit of magic that goes on here. bzr supports the ``--fixes``
option to commit. This marks the resulting revision as fixing the specified
bug, for example ``--fixes lp:301952`` would indicate that we closed the bug
that we are working on in this revision. In Intrepid (thanks to the idea
from Colin Watson) I implemented support for this in ``debcommit``. If
``debcommit`` sees you closing a bug in the changelog message that it is
using it will automatically add the corresponding ``--fixes`` argument (it
works for Debian bugs too).  We'll see where this comes in useful in a minute.

The last step is to get our changes in to the distribution. If we have upload
rights for the package then we can dput our source package that we created
a minute ago, and then run

::

  $ bzr push lp:ubuntu/jaunty/gnome-utils

to push the bzr branch back. (Yes, launchpad plans to support building directly
from a branch, so you just need to push along with some undecided mechanism to
request it be included in Ubuntu)

If you don't have upload rights for the package then you need someone to
sponsor the change for you. To do this you first push your branch to launchpad
somewhere under your name. For instance I would run

::

  $ bzr push lp:~james-w/ubuntu/jaunty/fix-301952

Note that thanks to the launchpad and bazaar developers implementing support
for "stacked branches" and automatic stacking in launchpad this will be a
very cheap operation, only pushing a single revision.

Next we would create a merge proposal for this change. You can either do this
from the branch page on launchpad, or you can use ``bzr send``. Just running

::

  $ bzr send

should do the right thing. It will open up a new message in your mail client.
You then enter your "cover letter" for the change, and hit send. It will
mail the request to launchpad which will interpret the machine-readable
attachment and turn it in to a merge request. The developers can then
review the changes and either ask for improvements to be done, or upload
the package.

Remember the ``--fixes`` information that was stored? That was also used by
launchpad. The bug that we were fixing now has a link to our branch on it,
so that anyone that wants to test the fix can find the right place to get
the change from. This currently does not generate any bugmail though, so
you have to go to the page to see it. I think this is something we need
to improve.

Some of the things that I have explained here haven't been fully decided,
so this isn't documentation, that will come later, the intent is to give
an idea of how this may work.

I've been asked a few times about an IRC channel where we can discuss this
sort of thing, so I created #ubuntu-bzr today. If you are interested in
shaping how this will work then please join it and we can discuss it. Support
can continue anywhere though.

