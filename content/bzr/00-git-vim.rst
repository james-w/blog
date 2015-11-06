Version control systems and text editors


So apparently "`learning git is like learning vim`_". Putting aside
the incremental learning aspects of this, and stretching the point
a little, will you allow me to say "git is like vim"?

.. _learning git is like learning vim: http://chistera.yi.org/~adeodato/blog/entries/2008/03/05/one_day_with_git.html

We all understand there is no way in which you would mandate that
all contributors use vim. You wouldn't want to lose all of those
valuable contributions from emacs users of course. However, you
still wouldn't dream of mandating the use of one of these two
editors. Why should your choice as project maintainer constrain
the way in which others want to work?

Obviously it is quite difficult to enforce this editor rule. For
a start there is nothing in a plain text file that tells you what
editor was used to create it. More importantly though, the
contributor's choice of editor doesn't matter to you. If they send
you a plain text file then your editor will handle it just as well
as theirs.

This is where version control differs from editors. When using the
version control system to move code around it tends to dictate the
client you use to access it, so one person's decision tends to
impact on others.

Is the solution therefore to work towards a situation we have
that is similar to that we have with text editors, where the
`interchange format`_ is understood equally well by all of the tools?
Do we spend time developing `wrappers`_ for `each use`_ that allow
us to ignore the fact that we are using different systems?

.. _interchange format: http://www.kernel.org/pub/software/scm/git/docs/git-fast-import.html
.. _wrappers: http://wingolog.org/archives/2008/03/11/using-newfangled-version-control-systems-from-emacs
.. _each use: http://kitenet.net/~joey/code/mr/

Recently there has been `work` done to make bzr support the
git-fast-import format. This would then be the start of an
interchange format that all tools could use to communicate.
However, the problem is that the representations used in one
system start to bleed. For instance, bzr supports ghosts, and we
are currently discussing the adding support to the format
to represent them. However git doesn't support them, and as
such there will be know way to complete a round trip of
bzr->git->bzr when there are ghosts involved.

.. _work: https://launchpad.net/bzr-fastimport

So, what about the other solution? Creating wrappers that
allow the user to not care what VCS they are using and just
get the job done? I think this is useful to a point. It will
be great for some people who just want to do really simple
things on lots of projects (for instance in Debian). However
the tools are necessarily catering to the lowest common
denominator, they won't support any of the unique things
that make each system great.

Bazaar has foreign branch support (most notably `bzr-svn`_)
which allow you to access another system as if if were bzr.
This is almost completely transparent ("bzr branch svn://"
makes it clear what the project is hosted in), in contrast
to git-svn. The latter adds a new command that allows you to
do the svn specific parts (setting up the repository, committing
back to svn). In contrast bzr-svn uses the normal bzr commands
for (almost[1]) everything, meaning you only need to learn the
one tool. git-svn is still a great tool, but it certainly makes
you realise that you are not dealing with pure git.

.. _bzr-svn: https://launchpad.net/bzr-svn

The competition between the systems has been great for every
one of them. However, it seems like we will be stuck with different
systems for the forseeable future, so we should work hard on
making them work well together to ease the pain on the users.
I think that many of the supporters of distributed version
control would say that it is better for you to be using any
of them than none of them, but the fractured and unstable
landscape we have now is causing a resistance in people to
make the switch.

.. [1] It currently adds svn-push for doing a push that creates
       a new branch in svn, but this is only a temporary thing,
       "bzr push" will be able to do this at some point. The other
       commands that are added are for extra things that the core
       bzr is not meant to deal with.


