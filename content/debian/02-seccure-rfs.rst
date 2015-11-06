seccure in Debian?

<p>
An <a href="http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=378987">RFP</a> 
was filed for <a href="http://point-at-infinity.org/seccure/">seccure</a>, a
small program allowing ECC based public-key crypto. I snapped it up and
produced a <a href="http://jameswestby.net/debian/">package</a>. The packaging
was simple, but I enjoyed playing with the software while I was doing it.
</p>

<p>
The upstream author, B. Poettering, has been fantastic, very responsive and
helpful. He even asked what features I would be interested in for the
software.
</p>

<p>
He wrote it for backups, and so it is quite simple, without the keyrings etc. 
of gpg. It might be quite useful, and the length of the keys makes it easy to
pass them around. I have put my key in my .signature for a bit of advertising.
ECC is planned to be included in a future version of gpg, so seccure will stay
small.
</p>

<p>
I also asked the <a href="http://shellcode.org/mailman/listinfo/debian-audit">
debian-audit</a> team if they would take a look at the package. Ulf Harnhammar
and Brian M. Carlson had a <a
href="http://shellcode.org/pipermail/debian-audit/2006-August/000319.html">
look</a>, and said that it was very well done.
</p>

<p>
I think there is a dictionary attack on the password, and so the secret key,
so you better pick a good one. My public key is 
<blockquote><p>
(3+)k7|M*edCX/.A:n*N!&gt;|&amp;7U.L#9E)Tu)T0&gt;AM
</p></blockquote>
using the secp256r1/nistp256 curve.
</p>

<p>
I currently have an open <a
href="http://lists.debian.org/debian-mentors/2006/07/msg00390.html">RFS</a> for the package, but I need to update it, as
there is a new upstream release, including an implementation of DH key
exchange.
</p>

