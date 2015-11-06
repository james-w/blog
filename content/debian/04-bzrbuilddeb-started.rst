bzr-builddeb started

The other day I decided I wanted to try out one of the more modern revision
control systems. I decided on `bzr`_ as it seemed to have some features that I
liked the look of. I still intend to try out `darcs`_ one day though, as it
looks very interesting.

.. _bzr: http://bazaar-vcs.org/
.. _darcs: http://abridgegame.org/darcs/

Just as I started looking at it and thinking about using it for some of my 
packaging work, I discovered that there was no -buildpackage for bzr. But lo, 
`madduck`_ filed an `ITP`_ for it. However he said that it didn't actually 
exist yet. 

.. _madduck: http://blog.madduck.net/
.. _ITP: http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=380198

I decided I would try and help to write something, even though I have hardly 
ever touched Python before. It was quite easy to hack something together by 
looking in examples. I ended up with a plugin that worked for me to build 
simple packages from a bzr repository, including supporting the layout where
just the debian/ dir is versioned (the mergeWithUpstream of svn-buildpackage). 
You can find my work `here`_, (in a bzr branch of course). The plugin is 
actually called builddeb, as it seems Fedora are keen on something similar, 
and so we didn't want to hog the namespace. The Debian package will probably
include a wrapper script named bzr-buildpackage though.

.. _here: http://jameswestby.net/bzr/builddeb/builddeb.dev

There is plenty that can be added on, for instance config files are needed, 
and madduck would like to include hook script capability within the branches,
but this is going to take some careful thought. 

I have quite enjoyed working in Python, it allows you to do things "properly"
if you want, but also can be very terse. I've not grasped all of the features
yet though.

