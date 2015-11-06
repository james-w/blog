Revision numbers
################

:date: 2008-03-13 16:49
:slug: bzr/01-revision-numbers


Revision numbers vs. revision ids
---------------------------------

One thing that Bazaar does a little different to the other distributed
systems is to give every revision a revision number. Some people don't
like this as the revision numbers are global, that means that the revision
number of a revision in my branch does not necessarily match the
number that it was given in your branch. Some people say that this
makes bzr somehow "less distributed." This is not the case at all,
you just need to be careful to be clear what branch you are referring
to, i.e. say "revision 315 on branch http://...", rather than just
"revision 315".

This is a little dangerous in that the branch may have it's revision
history changed, for instance by uncommitting and then committing
again. If that may happen then you should use revision ids, which
you can find from "bzr log --show-ids".

Why do number the revisions at all then? One reason is simply
that some people find revision ids ugly, and may be scared off
by them.

Another reason is that they are shorter to type. git folks will
tell you can use the first few characters of the revision id, and
git will work out what revision you mean. However these shortened
ids are not necessarily stable over a long period of time, and
so again, if you are worried you should use the whole thing.

The third reason is that the numbers can give some sense of the
order of the revisions in your branch. If I say talk about
revisions "3445abe" and "b27ac9" then you don't know which
is earlier in history. If I refer to revisions 345 and 532 then
it is immediately obvious (providing that I am only referring to
a single branch).

The advantages I have outlined are small, but they could be
valuable at times, and you always have the revision ids to fall
back on if you require them.

Numbering merged revisions
--------------------------

Along with numbering the mainline bzr also numbers merged revisions
using a dotted numbering scheme. This means that your mainline
revisions are "1", "2", "3", as you would expect, but any merged
revisions are given three digit numbers, e.g. "2.1.3".

The numbering scheme has a couple of nice properties, the most
notable of which is that it is "stable", this means that once
I have numbered a merged revision with respect to a certain mainline
it cannot be effected by any addition I make to the revision history.
This means that any commits, pulls or merges that I do will not
change any of the existing revision numbers, but they will add
numbers to any new merged revisions such that they will not be
the same as any number already used.

The current algorithm used for this involves looking at the whole
history of the branch to number the revisions, which is obviously
undesirable.

On the last evening of the sprint last week myself and John
were discussing the numbering scheme, and thinking about
possible algorithms to do the numbering that would be more
efficient.

We had the following inputs:

  1. The revsision id you are trying to give a dotted number
     for.
  2. The tip of the mainline that you are numbering against.
  3. The revision number of that mainline revision.
  4. A map of revision_id -> parents.

And you are asked to provide the revision number for the specified
revision. Any other numbering that you may be able to do along the
way would be a bonus.

The fact that all we are given to get the information we need is
a map telling us the parents of a revision id means that we cannot
ask the question "what are all the children of this revision?"

I don't really want to explain the numbering scheme here, as it
is a little long-winded to do so. The outline is that for the first
digit you find the intersection of the target revision's left hand
ancestry with the mainline, and use its revision number. For the
second digit you find all of the branches that originated at the
revision found in the first part, and then number them by
the order that they merged back in to mainline. The third
digit is then just the place of the revision in its own part
of one of these branches.

Notice the second step there. Remember that we are not able to
retrieve the children of any revision? That means that we must
work backwards from our mainline to do this. This is where
the real complexity comes in, and it appears as though it is
necessary to search a reasonable amount of history to
calculate this part.

After the discussion with John I had a reasonable idea of how
such an algorithm would work, and yesterday I posted a `first
draft`_ of that to the mailing list. We have found some
problems with it, and haven't benchmarked it yet to see if it
is actually an improvement, but hopefully it will evolve and
prove to be faster.

.. _first draft: http://thread.gmane.org/gmane.comp.version-control.bazaar-ng.general/38388

Displaying logs, and history emphasis
-------------------------------------

The revision numbering code has a very close relationship,
and also interacts with it in an awkward way from a 
performance standpoint. This lead to John explaining
to me how the logs are generated in more depth.

When bzr produces logs by default it emphasises the left
hand parent to produce your mainline. It then indents any
revisions that you merged::

>       -----------------------------------------------------------
>	revno: 3270
>	committer: Canonical.com Patch Queue Manager <pqm@pqm.ubuntu.com>
>	branch nick: +trunk
>	timestamp: Thu 2008-03-13 00:40:30 +0000
>	message:
>	  (Adeodato Simo) Add a space after "revision-id:" in log output.
>          -----------------------------------------------------------
>	   revno: 3257.2.1
>	   committer: Adeodato Simó <dato@net.com.org.es>
>	   branch nick: foo
>	   timestamp: Sun 2008-03-09 23:06:47 +0100
>	   message:
>	     Add a space after "revision-id:" in log output.
>       -----------------------------------------------------------
>	revno: 3269
>	committer: Canonical.com Patch Queue Manager <pqm@pqm.ubuntu.com>
>	branch nick: +trunk
>	timestamp: Wed 2008-03-12 23:08:34 +0000
>	message:
>	  (Daniel Watkins) Add a --revision option to 'bzr push'
>           -----------------------------------------------------------
>	    revno: 3256.1.5
>	    committer: Daniel Watkins <D.M.Watkins@warwick.ac.uk>
>	    branch nick: push-r
>	    timestamp: Sun 2008-03-09 18:41:31 +0000
>	    message:
>	      Added NEWS entry.


To do this it must decide which revisions are present in the history
of one revision, but not in the history of its left hand parent.
To do this it starts off two history walkers in parallel, one
walking the history of the first revision, the second walking the
history of the parent. The first walker then stops walking down
a particular line of history when the second "claims" it, once
the first walker has no more lines of history to walk it returns
its group of revisions, and the log formatter code then displays them
indented as necessary to match the history.

This is a much more complex process than that you get with "git log",
in which the revisions are produced in just `date order`_. There is
a "--topo-order" option to git log, but that just ensures that all
parents are output before their children. It doesn't ensure that
all parents not in the ancestry of the left-hand parent are shown
before the left-hand parent. The work to ensure that is significantly
more than that done to provide "--topo-order".

.. _date order: http://news.gmane.org/gmane.comp.version-control.git

This display makes it easy to see what work was done on a branch,
and when those changes entered your branch. This is one reason
why bzr's merge doesn't fast-forward by default ("bzr merge --pull"
will do this for you if you like). This means that you can always
instantly identify which work came from another branch and have
them tied together.

Always having merge commits means that "bzr log --short" and
"bzr log --line" can give you a good summary of what happened
on your branch, the commits you did, and the things that you
merged. It preserves a mainline for you in the left hand
ancestry, which means that you can always see what happened
in that particular branch. "bzr pull" then gives you a mirror
of another branch, and the left hand ancestry tells you what
happened in that branch.

The indentation of the merged commits (and the fact they
disappear with "--short" and "--line") means that mentally
they become of lesser importance. You see "merged performance
work from Emma's branch", rather than all of the commits that
you got from her. They are still there to look at if you want,
but they can be ignored at most times.

This means that you don't have to spend time rewriting history
to be clean if you don't want to. You don't have the
history right in your face either way, though there can 
still be value in having a clean history. However rewriting
history is not what some people `want`_ to `do`_, and causes
problems for those who base their work on yours.

.. _want: http://lists.debian.org/debian-devel/2008/02/msg01053.html
.. _do: http://lists.debian.org/debian-devel/2008/03/msg00236.html

