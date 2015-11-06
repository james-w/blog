pkgme: handles packaging for you
################################

:date: 2011-02-06 19:05
:slug: tech/23-pkgme-handles-packaging-for-you

If you are an application developer and you want to distribute your new
application for a linux distribution, then you currently have several
hurdles in your path. Beyond picking which one to start with, you either
have a learn a packaging format well enough that you can do the work
yourself, or find someone that can do it for you.

At the early stages though neither of these options is particularly
compelling. You don't want to learn a packaging format, as there is
lots of code to write, and that's what you want to focus on. Finding
someone to do the work for you would be great, but there are far
more applications than skilled packagers, and convincing someone to
help you with something larval is tough: there are going to be a lot
of updates, with plenty of churn, to stay on top of, and it may be
too early for them to tell if the application will be any good.

This is where ``pkgme`` comes in. This is a tool that can take care
of the packaging for you, so that you can focus on writing the code,
and skilled packagers can focus on packages that need high-quality
packaging as they will have lots of users.

This isn't a new idea, and there are plenty of tools out there to
generate the packaging for e.g. a Python application. I don't
think it is a particularly good use of developer time to produce
tools like that for every language/project type out there.

Instead, a few of us created ``pkgme``. This is a tool in two parts.
The first part knows about packaging, and how to create the necessary
files to build a working package, but it doesn't know anything about
your application. This knowledge is delegated to a backend, which doesn't
need to understand packaging, and just needs to be able to tell ``pkgme``
certain facts about the application.

``pkgme`` is now at a stage where we would like to work with people to
develop backends for whatever application type you would like (Python/
Ruby On Rails/GNOME/KDE/CMake/Autotools/Vala etc.) You don't have to
be an expert on packaging, or indeed on the project type you want to
work on. All it takes is writing a few scripts (in whatever language
makes sense), which can introspect an application and report things
such as the name, version, dependencies, etc.

If this sounds like something that you would like to do then please
`take a look at the documentation`_, write the scripts, and then
submit your backend for inclusion in ``pkgme``.

.. _take a look at the documentation: http://pkgme.net/doc/backends/index.html

You can also `contact the developers`_, see the `nascent website at pkgme.net`_,
or `visit the Launchpad page.`_ (We are also very interested in help
with the website and documentation if that is where you skills or interests
lie.)

.. _contact the developers: http://pkgme.net/contact.html
.. _nascent website at pkgme.net: http://pkgme.net/
.. _visit the Launchpad page.: https://launchpad.net/pkgme
