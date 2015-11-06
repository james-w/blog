Daily Builds
############

:date: 2009-08-04 12:58
:slug: ubuntu/11-daily-builds

As well as seeing use of PPAs for providing bug fixes, new upstream versions, proposed packages, testing etc., we are also seeing them used for providing daily builds of packages. For instance `Fabien Tassin`_ provides daily builds of lots of Mozilla-related packages and snapshots of Chromium in his various PPAs. Also, there is `Project Neon`_, to provide daily builds of Amarok.

.. _Fabien Tassin: https://edge.launchpad.net/~fta
.. _Project Neon: http://amarok.kde.org/en/node/482

They massively lessen the barrier to using and testing code that is fresh from the fingers of the developers. They avoid you having to build a project from source every day, making sure to keep up with changes in dependencies. They allow you to be testing code almost as it is written, speeding up the feedback cycle to the developers, and potentially increasing the number of people involved in that feedback cycle.

In addition they allow you to verify bugs against the latest code, so that bug reports are of more relevance to the developers. If you so choose they can also be set up so that bugs are also tested with fewer distribution patches, further increasing the developers' confidence in the bug reports. 

Mark had an idea for an elegant way to describe how to combine the code to produce the package, and we worked on producing a tool to follow the steps. You can find the result of this in the bzr plugin `bzr-builder`_. I've `documented how to use it`_ on the wiki.

.. _bzr-builder: https://launchpad.net/bzr-builder
.. _documented how to use it: https://wiki.ubuntu.com/DailyBuilds/BzrBuilder

There's still more we can do to improve the process, and we have a lot to discuss about what makes a good daily package, and what the limits of them are. If you are interested in discussing this then please join the list of the `dailydebs team in Launchpad`_.

.. _dailydebs team in Launchpad: https://launchpad.net/~dailydebs-team

I'm currently running the `bzr-nightly-ppa`_ using this tool, and have improved some things based on this, but more testing, feedback, and patches are always welcome.

.. _bzr-nightly-ppa: https://launchpad.net/~bzr-nightly-ppa/+archive/ppa
