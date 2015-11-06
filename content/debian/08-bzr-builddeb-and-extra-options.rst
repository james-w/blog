bzr-builddeb and extra options

I spent today hacking on bzr-builddeb for the first time in a while. The
first order of business was to review and merge all of the `proposed merges`_
in launchpad. Thanks especially to `Jelmer Vernooij`_ for all his work.

.. _proposed merges: https://code.launchpad.net/bzr-builddeb/+activereviews
.. _Jelmer Vernooij: http://jelmer.vernstok.nl/blog/

After that I tackled a long-standing `annoyance`_ in bzr-builddeb. This
limitation made it difficult to pass extra options to the underlying
build command. For instance, when building a merge you must use the ``-v``
option to ``debuild``. Previously this meant that you would have to run 
something like::

  $ bzr builddeb -S --builder "debuild -S -v0.1-1"

.. _annoyance: https://bugs.edge.launchpad.net/bzr-builddeb/+bug/248640

Using the tradition of ``--`` to end option parsing this now becomes::

  $ bzr builddeb -- -S -v0.1-1

which is much better.

The ``--`` isn't exactly obvious, but it does mean that I don't have to
implement support for every option of dpkg-buildpackage.

It may be possible to add support in bzr to make this work without the
``--``, I haven't looked yet, and the current implementation doesn't
prevent us from doing that.

One other thing I did was to make the build command default to ``debuild``,
rather than ``dpkg-buildpackage -rfakeroot -uc -us``, so that we get all
the ``debuild`` goodness. The obvious change here will be that it tries to
sign the package when you build. You can define your builder to be
``debuild -uc -us`` to avoid this.

One last break was to remove support for ``source-builder`` from the
configuration. It now assumes that adding ``-S`` to the build command
will make it build a source package.

Comments on any of this are welcome.
