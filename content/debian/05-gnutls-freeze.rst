GnuTLS freeze for etch


We hadn't really realised but some gnutls related packages are ``Priority:
Important``, and as such are due to be frozen soon for etch. There has been
some upstream activity in the area recently, with several releases. Luckily
the timing was really good, and the uploads made it in such that they should
progress to etch quickly, without causing any trouble for the release team.

Also there has been some action from a couple of the maintainers holding up
the gnutls11 and libtasn1-2 removal. This just leaves two packages, one of
which the maintainer has tagged pending, and `nutmeg`_ has just upgraded the 
bugs to serious to try and prod the maintainers. It is possible then that
removal can be requested before the release team calls the freeze that is
supposed to include these packages.

.. _nutmeg: http://downhill.g.la/blog/

gnutls13 builds a gnutls-dev package, which will make this easier in the
future... until there is an API change and we have to switch back to
gnutlsXX-dev and get all packages to migrate again. It is hard to know which
is the better approach, but at least this way it only requires rebuilds while
things stay calm.

