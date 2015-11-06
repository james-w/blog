ppamadison
#parser reST

After an idea from bigon on #launchpad today I threw together a tool
using the `Launchpad API`_. I've christened this tool ``ppamadison``.
It does the same thing as ``rmadison``, but for PPAs. You tell it
who's PPA to examine, and what source package to get the information
for, and it tells you what versions are available.

.. _Launchpad API: https://help.launchpad.net/API

::

	$ ppamadison james-w bzr-builddeb
	bzr-builddeb | 2.0~0ubuntu1~ppa1 | intrepid | source
	bzr-builddeb | 2.0~ppa1~hardy1 | hardy | source

There's still some things left to do, such as replicating rmadison's odd
output formatting, some things missing from the Launchpad API and some
interesting things you could add, but the idea is there. One thing
missing from the Launchpad APIs as far as I can see is an efficient
way to find out which PPAs contain a certain source package name.
This would be quite an interesting thing to know.

Would ppamadison be a useful thing to have in ``ubuntu-dev-tools``?
If it is worthwhile then I will integrate it. Because this blog post
is something that developers might not see, but might be interested in
I would then pass it on to the `Developer News`_ service, as all it
would take would be a quick email, as little as a link to the blog
post would do.

.. _Developer News: https://wiki.ubuntu.com/UbuntuDevelopment/News

(Yes, I am being facetious, but we haven't had a single submission yet)

As an aside, I play with the Launchpad APIs every couple of months
and they are getting better, to the point now where most data I want
for things I do is available. Thanks to the Launchpad team for their
work on it. There are some real problems for some use-cases, such as
a cache hit requiring a https connection, but ways can be found to
deal with them. In any case, the APIs will allow us to do some really
useful things.

P.S. Thank you all for your kind words.

