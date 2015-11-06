Project Cambria
###############

:date: 2010-02-01 01:35
:slug: ubuntu/15-project-cambria

`David`_, it's interesting that you posted about that, as it's something I've been toying with
for the last couple of years. For the last few months I've been (very) slowly experimenting
in my free time with an approach that I think works well, and I think it's time to tell more
people about it and to ask for contributions.

.. _David: http://davidsiegel.org/improving-bug-workflow-for-opportunistic-programmers/

Opportunistic programmers are useful to cater for here, as Debian/Ubuntu development isn't trivial,
and so we are simplifying something existing, which means that it will still be powerful, which
is also important. I'm not only interested in improving the experience for the opportunistic
programmer though, why should they get all the cool stuff? I'm interested in producing something
that I can use for doing Ubuntu development too (though not every last detail).

The project I am talking about has been christened "cambria" and is now `available on Launchpad`_.
It's a library that aims to provide great APIs for working with packages throughout the lifecycle,
including things like Bazaar, PPAs, local builds, testing, lintian, etc. It should be pleasurable
to use and also allow you to build tools on top that are also pleasurable. It should also allow
for easy extension in to different GUI toolkits and for command-line tools, though I've only been
working with GTK so far.

.. _available on Launchpad: https://launchpad.net/cambria

In addition, there is a `gedit plugin`_ that allows you to perform common tasks from within gedit.
I chose gedit as it has a pleasant Python API for plugins, isn't so complicated that it takes much
learning, and will already be installed on most Ubuntu desktop systems. As I said though, the libarary
allows you to implement in anything you like (that can use a python library.)

.. _gedit plugin: https://launchpad.net/gedit-ubudev

I've put together some mockups that suggest some of the things that I would like to do:

.. image:: /images/build-thumb.png
   :alt: A mockup of an inteface for building packages within gedit. There is a button to build the active package, and a box that shows the output of the build.

Build_

.. _Build: /images/build.png

.. image:: /images/package-list-thumb.png
   :alt: A mockup of an inteface for jumping to work on packages already downloaded in gedit. There is a list of packages that have previously been worked on, and the user can choose any to open a dialog of the contents of that package to choose a file to edit from within.

`Package list`_

.. _Package list: /images/package-list.png

.. image:: /images/download-thumb.png
   :alt: A mockup of an inteface for downloading the source of packages within gedit. The main point conveyed is that the user should be asked what they intend to work on (bug fix, merge, etc.) so that the tools can do some of the work for them, and wizards and the like can be used to do the rest.

`Download`_

.. _Download: /images/download.png

`The RATIONALE file`_ includes some more reasons for the project:

  Project cambria is about wrapping the existing tools for Debian/Ubuntu
  development to allow a more task-based workflow. Depending on the task the
  developer is doing there may be several things that must be done, but they
  must currently work each one out individually. We have documentation to help
  with this, but it's much simpler if your tools can take care of it for you.
  
  Project cambria aims to make Ubuntu development easier to get started with.
  There are several ways that it will help. Providing a task-based workflow
  where you are prompted for the information that is needed to complete the
  task, and other things are done automatically, or defaults chosen helps as
  it means you can concentrate on completing the task, rather than learning
  about all the possible changes you could make and deciding which applies.
  
  Project cambria aims to make Ubuntu development easier for everyone by
  automating common tasks, and alleviating some of the tool tax that we pay.
  It won't just be a beginner tool, but will provide tools and APIs that
  experienced developers can use, or can build upon to build tools that suit
  them.
  
  Project cambria will help to take people from novice to experienced
  developer by providing documentation that allows you to learn about the
  issues related to your current task. This provides an easier way in to the
  documentation than a large individual document (but it can still be read
  that way if you like).
  
  Project cambria will make Ubuntu development more pleasurable by focusing
  on the user experience. It will aim to pull together disparate interfaces
  in to a single pleasing one. Where it needs to defer to a different interface
  it should provide the user with an explanation of what they will be seeing
  to lessen the jarring effect.

.. _The RATIONALE file: http://bazaar.launchpad.net/~cambria-dev/cambria/trunk/annotate/head:/RATIONALE

I'm keen for others to contribute, there is some information about this in
`the project's CONTRIBUTING file`_. I'm looking for all sorts of contributions
from all kinds of people and keen to help you get started if you aren't confident
with the type of contribution you would like to make.

.. _the project's CONTRIBUTING file: http://bazaar.launchpad.net/~cambria-dev/cambria/trunk/annotate/head:/CONTRIBUTING

There's a mailing list as part of `the ~cambria team`_ on Launchpad and IRC channel
if you are interested in discussing it more.

.. _the ~cambria team: https://launchpad.net/~cambria
