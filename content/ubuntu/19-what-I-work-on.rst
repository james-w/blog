What I work on
##############

:date: 2010-09-14
:slug: ubuntu/19-what-I-work-on

I'm keen to try and write more about the things that I work on as part of my
job at Canonical. In order to get started I wanted to write a summary of some
of the things that I have done, as well as a little about what I am working on
now.

Ubuntu Distributed Development
------------------------------

This isn't the catchiest name for a project ever, and has an unfortunate collision
with an `Debian project`_, also shortened to "UDD." However, the aim is for this
title to become a thing of the past, and this just to be the way things are done.

.. _Debian project: http://udd.debian.org/

This effort is firstly about getting Ubuntu to use Bazaar, and a suite of associated
tools, to get the packaging work done. There are multiple reasons for this.

First, and most simply, is to give developers the power of version control as they
are working on Ubuntu packages. This is useful for both the large things and the
small. For instance I sometimes appreciate being able to walk through the history
of a package, comparing diffs here and files there when debugging a complex problem.
Sometimes though it's just being able to "bzr revert" a file, rather than having
to unpack the source again somewhere else, extracting the file and copying it over
the top.

There are higher purposes with the work too. The goal is to link the packaging
with the upstream code at the version control level, so that one flows in to
the other. This has practical uses, such as being able to follow changes as
they flow upstream and back down again, or better merging of new upstream
versions. I believe it has some other benefits too, such as being able to see
the packages more clearly as what they are, a branch of upstream. We won't just
talk about them being that, but they truly will be.

Some of you will be thinking "that's all well and good, but <project> uses git,"
and you are absolutely right. Throughout this work we have had two principles
in mind, to work with multiple systems outside of Ubuntu, and to provide a
consistent interface within Ubuntu.

Due to the way that Ubuntu works an Ubuntu developer could be working on any
package next. I would really like it if the basics of working with that package
were the same regardless of what it was. We have a lot of work to do on the
packaging level to get there, but this project gets this consistency on the
version control level.

We can't get everyone outside of Ubuntu to follow us in this though. We have to
work with the system that upstream uses, and also to work with Debian in the
middle. This means that we have to design systems that can interface between
the two, so we rely a lot on Launchpad's bzr code imports. We also want to
interface at the other end as well, at "push" time. This means that if an
Ubuntu developer produces a patch that they want to send upstream they can
do that without having to reach for a possibly different VCS.

Thanks mainly to the work of Jelmer Vernooij we are doing fairly well at being
able to produce patches in the format appropriate for the upstream VCS, but we
still have a way to go to close the loop. The difficultly here is more around
the hundreds of ways that projects like to have patches submitted, whether it
is a mailing list or a bug tracker, or in some other form. At this stage
I'd like to provide the building blocks that developers can put together as
appropriate for that project.

Daily package builds
--------------------

Relatedly, but with slightly different aims, I have been working on a project in
conjunction with the Launchpad developers to allow people to have daily builds of
their projects as packages.

Currently there is too often a gap between using packaged versions of a project,
and running the tip of that project daily. I believe that there are lots of people
that would like to follow the development of their favourite projects closely,
but either don't feel comfortable building from the VCS, or don't want to go through
the hassle.

Packages are of course a great way to distribute pre-compiled software, so it was
natural to want to provide builds in this format, but I'm not aware of many projects
doing that, aside from those which `fta`_ provides builds for. Now that Launchpad
provides PPAs and code imports, and the previous project provides imports of the
packaging of all Debian and Ubuntu packages in to bzr, all the pieces are there
in order to allow you to produce packages of a project automatically every day.

.. _fta: https://launchpad.net/~fta

This is currently available in beta in Launchpad, so you can go and `try it out`_,
though there are a few known problems that we are working on until it will be
as pleasant as we want.

.. _try it out: https://help.launchpad.net/Packaging/SourceBuilds/Recipes

This has the potential to do great things for projects if used correctly. It can
increase the number of people testing fresh code and giving feedback by orders
of magnitude. Also, just building the packages acts as a kind of continuous
integration, and can provide early warning of problems that will affect the
packaging of the project. Also, they provide an easy way for people to test
the latest code if a bug is believed to be fixed.

Obviously there are some dangers associated with automatic builds, but if they
are used by people who know what they are doing then it can help to close
the loop between users and developers.

There are also many more things that can be done with this feature by people
with imagination, so I'm excited to see what directions people will take
it in.

Fixing things
-------------

Aside from these projects, I was also given some time to work on Ubuntu itself,
but without long-term projects to ship. That meant that I was able to fix things
that were standing in my way, either in the way of the above projects, or just
hampering my use of Ubuntu, or fix important bugs in the release.

In addition I took on smaller projects, such as getting kerneloops enabled by
default in Ubuntu. While doing this I realised that the user experience of that
tool could be improved a lot for Ubuntu users, as well as allowing us to report
the problems caught by the tool as bugs in Launchpad if we wished.

I really enjoyed having this flexibility, as it allowed me to learn about many
areas of the Ubuntu system, and beyond, and also played to my strengths of
being able to quickly dive in to a new codebase and diagnose problems.

I think that in my own small way, each of these helped to improve Ubuntu releases,
and in turn the projects that Ubuntu is built from.

Sponsoring
----------

While I'm sorry to say that other demands have pulled my code review time in to
other projects, I did used to spend a lot of time reviewing and sponsoring changes
in to Ubuntu.

I highlight this mainly as another chance to emphasise how important I think code
review is, especially when it is review of code from people new to the project.
It improves code quality, but is also a great opportunity for mentoring,
encouraging good habits, and helping new developers join the project. I hope
that my efforts in this are had a few of these characteristics and helped increase
the number of free software developers. Oh how I wish there were more time to
continue doing this.

Linaro
------

I've now been started working on the Linaro project, specifically in the Infrastructure
team, working on tools and Infrastructure for Linaro developers and beyond. I'm not one
to be all talk and no action, so I won't talk to much about what I am working on, but
I would like to talk about why it is important.

Firstly I think that Linaro is an important project for Free Software, as it has the
opportunity to lead to more devices being sold that are built on or entirely
free software, some in areas that have historically been home to players that have
not been good open source citizens.

Also, I think tools are an important area to work on, not just in Linaro. They pervade
the development experience, and can be a huge pain to work with. It's important that
we have great tools for developing free software so as not to put people off. Developers,
volunteers and paid, aren't going to carry on too long with tools that cause them more
problems than they are worth, and not all are going to persist because they value
Free Software over their own enjoyment of what they do.
