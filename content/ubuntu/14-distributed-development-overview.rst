Ubuntu Distributed Development Overview
#######################################

:date: 2009-12-16 22:49
:slug: ubuntu/14-distributed-development-overview

You may well have heard about it (on this blog especially),
but though I spend lots of my time involved with it and talking
to people about it, there may be some people who aren't
entirely sure what we are doing with the Ubuntu Distributed
Development initiative, or what we are trying to achieve.
To try and help this I wrote up an overview of what we are
doing.

If this project interests you and you would like to help, or
just observe, then you can `subscribe to the mailing list`_.
There's lots of fun projects that you could take on: there's
far more that is possible and would be hugely useful to Ubuntu
developers than we can currently work on. If you want to work
on something then feel free to talk to me about it and we
can see if there is something that would suit you.

.. _subscribe to the mailing list: https://lists.ubuntu.com/mailman/listinfo/ubuntu-distributed-devel

Without further ado...

The aim
=======

The TL;DR version:

  1) Version Control rocks.
  2) Distributed version control rocks even more.
  3) Bazaar rocks particularly well.
  4) Let's use Bazaar for Ubuntu.

Or, if you prefer a more verbose version...

Ubuntu is a global project with many people contributing to the development
of it in many ways. In particular development/packaging involves many people
working on packages, and much of this requires more than one person to work
on the change that it is being made, for e.g.

  1) Working on the problem together
  2) Sponsoring
  3) Other review

etc.

These things usually require the code to be passed backwards and forwards,
and in particular, merged. In addition, we sometimes have to do things
like merge the patch in the bug with a later version of the Ubuntu package.
In fact, Ubuntu is a derivative of Debian, and we expend a huge effort
every cycle merging the two.

Distributed version control systems have to be good at merging, it's a
fundamental property. We currently do without, but we have tools such
as MoM that use version control techniques to help us with some of the
merging. We could carry on in this fashion, or we could move to use
a distributed version control system and make use of its features, and
gain a lot of other things in the process.

Tasks such as viewing history, and annotating to find who made a particular
change and why, also become much easier than when you have to download and
unpack lots of tarballs.

This isn't to say that there aren't costs to the transition, and tools
and processes we currently use that don't currently have an obvious
analogue in the bzr world. That just means we have to identify those
things and put the work in to provide an alternative, or to port, where
it makes sense.

The aim is therefore to help make Ubuntu developers more productive, and
enable us to increase the number of developers, by making use of modern
technologies, in particular Bazaar, though there are several other
things that are also being used to do this.

What it isn't
=============

This isn't a project to overhaul all the Ubuntu development tools. While
there are many things I would like to fix about some of our tools (see
some of the things that Barry had to get his head around in the "First
Impressions" thread), that can go ahead without having to tie it in to
this project. I hope that when me make some common tasks easier, it will
focus attention on others that are still overly complex, and encourage
people to work on those too.

We are not replacing the entire stack. We are building upon the lower
layers, and replacing some of the higher ones. We aim for compatibility
where possible, and not breaking existing workflows until it makes
sense.

The plan
========

You can read the original overall specification for this work at

  https://wiki.ubuntu.com/DistributedDevelopment/Specification

It is rather dry and lacking in commentary, and also a little out
of date as we drill down in to each of the phases. Therefore I'll
say a little more about the plan here.

The plan is to work from the end of the Ubuntu developers, converting
the things that we work most directly with first. This should give the
biggest impact. We will then work to pull in other things that improve
the system.

This means that we start by making all packages available in bzr, and
make it possible to use bzr to do packaging tasks. In addition to this
we are working with the LP developers to make it possible for Soyuz to
build a source package from the branch, so that you don't have to leave
bzr to make a change to a package. This work is underway.

After that we make all of Debian available in bzr in the same way. This
allows us to merge from Debian directly in bzr. At a first cut, this
just allows us to replace MoM, but in fact allows for more than that.
Have a conflict? You have much more information available as to why
the changes were made, which should help when deciding what to do.

The next step after that is to also bring the Vcs-* branches in to the
history. These are the branches used by the Debian maintainer, and so
allow you to work directly with the Debian maintainer without switching
out of the system that you have learnt.

In a similar way we then want to pull in the upstream branches
themselves. Again, this will allow you to work closely with upstream,
without having to step out of the normal workflow you know.

The last point deserves some more explanation. The idea is that you
will be able to grab a package as you normally do, work on a patch,
and then when you are happy run a command or three that does something
like the following:

  * Merges your change in to the tip of upstream, allowing you to
    resolve any conflicts.
  * Provide a cover letter for the change (seeded with the changelog
    entry and/or commit message(s).
  * Send the change off to upstream in their preferred format and
    location (LP merge proposal, patch in the bugtracker, mailing list
    etc.)

As you can imagine, there are a fair number of prerequisites that we
need to complete before we can get to that stage, but I think of that
as the goal. This will smooth some of the difficulties that arise in
packaging from having to deal with a variety of upstreams. Finding the
upstream VCS, working out their preferred form and location for
submission, rebasing your change on their tip etc. I hope this will
make Ubuntu developers more efficient, make forwarding changes
easier to do and do well, and save new contributors from having to
learn too many things at once.

Where we are now
================

We currently have all of Ubuntu imported (give or take), you can

  bzr branch lp:ubuntu/<source package name>

which is great in itself for many people.

We also have all of Debian imported, and similarly available with

  bzr branch lp:debian/<source package name>

which naturally allows

  bzr merge lp:debian/<source package name>

so you can make use of that right now.

We are also currently looking at the sponsorship process around
bzr branches, and once we have that cracked it will be much easier
for upstream developers who know bzr to submit a bugfix, and that's
a large constituency.

In addition, this means that a new contributor can start without
having to learn debdiff etc., we can pass code around without having
to merge two diffs and the like.

This is great in itself, but we are still some way from the final
goal.

We are currently working on the VCS-* branches, to make them mergeable,
but their are a number of prerequisites.

In addition the Launchpad team are also working on making it possible
to build from a branch.

Where we can go
===============

As I said, building on top of bzr makes a number of things easier.

For instance, once LP can build from branches, we could have a MoM-a-like
that very cheaply tries to merge from Debian every time there is an
upload there, and if it succeeds build the package. This could then
tell you not only if there were any conflicts in the merge, but any
build failures, even before you download the code.

In addition, we are currently talking a lot about Daily Builds, building
the latest code every day (or commit, week, whatever). There are a number
of things this brings. It doesn't strictly require version control, but
as it's basically a merging problem having everything in Bazaar makes it
much easier to do. We have a system now built on "recipes" that we are
working to add to LP.

Parts of the work
=================

There are a number of parts to the work, and you will see these and
others being discussed on the list:

  * bzr (obviously), which we sometimes need to change to make this work
    possible, either bug fixes, or sometimes new features.
  * bzr-builddeb, which is a bzr plugin that knows how to go from branch
    to package and vice-versa.
  * bzr-builder, the bzr plugin that implements "recipes."
  * Launchpad, which hosts the branches, provides the merge prosals, and
    will allow building from branches and daily builds.
  * The bzr importer, this is the process that mirrors the Ubuntu and Debian
    archives in to bzr and pushes the branches to LP.

and probably others that I have forgotten right now.

