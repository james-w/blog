Setting up Icecast2 on Debian


Hannah is very interested in radio, and is planning to set up her own Internet
radio site. I wanted to try out icecast to see whether it would be suitable. I
have jotted down a few notes about how to set it up here as I couldn't see any
others.

Firstly get the server and the streaming client:

  aptitude install icecast2 ices2

Then edit ``/etc/default/icecast2`` to enable the daemon, and
``/etc/icecast2/icecast.xml`` to set the passwords.

Then 

  /etc/init.d/icecast2 start

Then 

  cp /usr/share/doc/ices2/examples/ices-playlist.xml .

and set the password in ``ices2-playlist.xml`` to be the stream password you
set above.

Then create ``playlist.txt`` with the names of some .ogg files, one per line.

Then run as root

  ices2 ices-playlist.xml

and test using 

   mplayer http://localhost:8000/example1.ogg

Hopefully this should be enough to get a stream going, and then you can
configure it how you want.



