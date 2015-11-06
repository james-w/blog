Re: Getting the hobbyist back
#############################

:date: 2010-04-30 14:59
:slug: tech/15-Re-Getting-the-hobbyist-back

Dear `Mr Neary`_, thanks for your thought provoking post, I think it is a
problem we need to be aware of as Free Software matures.

.. _Mr Neary: http://blogs.gnome.org/bolsh/2010/04/29/getting-the-hobbyist-back/

Firstly though I would like to say that the apparent ageism present in your
argument isn't helpful to your point. Your comments appear to diminish the
contributions of a whole generation of people. In addition, we shouldn't just
be concerned with attracting young people to contribute, the same changes will
have likely reduced the chances that people of all ages will get involved.

Aside from that though there is much to discuss. You talk about the changes in
Free Software since you got involved, and it mirrors my observations. While these
changes may have forced fewer people to learn all the details of how the system
works, they have certainly allowed more people to use the software, bringing many
different skills to the party with them.

I would contend that often the experience for those looking to do the compilation
that you rate as important has parallels to the experience of just using the software
you present from a few years ago. If we can change that experience as much as we
have the installation and first use experience then we will empower more people to
take part in those activities.

It is instructive then to look at how the changes came about to see if there are
any pointers for us. I think there are two causes of the change that are of interest
to this discussion.

Firstly, one change has been an increased focus on user experience. Designing
and building software that serves the users needs has made it much more palatable
for people, and reduced the investment that people have to make before using it.
In the same way I think we should focus on developer experience, making it more
pleasant to perform some of the tasks needed to be a hobbyist. Yes, this means
hiding some of the complexity to start with, but that doesn't mean that it can't
be delved in to later. Progressive exposure will help people to learn by not
requiring them to master the art before being able to do anything.

Secondly, there has been a push to make informed decisions on behalf of the user
when providing them with the initial experience. You no longer get a base system
after installation, upon which you are expected to select from the thousands of
packages to build your perfect environment. Neither are you led to download multiple
CDs that contain the entire contents of a distribution, much of which is installed
by default. Instead you are given an environment that is already equipped to do
common tasks, where each task is covered by an application that has been selected
by experts on your behalf.

We should do something similar with developer tools, making opinionated decisions
for the new developer, and allowing them to change things as they learn, similar
to the way in which you are still free to choose from the thousands of packages
in the distribution repositories. Doing this makes documentation easier to write,
allows for knowledge sharing, and reduces the chances of paralysis of choice.

There are obviously difficulties with this given that often the choice of tool
that one person makes on a project dicatates or heavily influences the choice
other people have to make. If you choose autotools for your projects then I can't
build it with CMake. Our development tools are important to us as they shape
the environment in which we work, so there are strong opinions, but perhaps
consistency could become more of a priority. There are also things we can do
with libraries, format specifications and wrappers to allow choice while still
providing a good experience for the fledgling developer.

Obviously as we are talking about free software the code will always be available,
but that isn't enough in my mind. It needs to be easier to go from code to
something you can install and remove, allowing you to dig deeper once you have
achieved that.

I believe that our effort around things like `https://dev.launchpad.net/BuildBranchToArchive`_
will go some way to helping with this.

.. _https://dev.launchpad.net/BuildBranchToArchive: https://dev.launchpad.net/BuildBranchToArchive

