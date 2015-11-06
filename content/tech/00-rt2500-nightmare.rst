Problems with rt2500 802.11 PCI card

<p>
A while ago now there was a power-cut in our area, and this took my box down
quite hard. The main effect of this was that my Belkin F5D7000UK PCI 802.11b/g
card stopped working. This was at a time when I was supposed to be working on
the wavelan plug-in for xfce as it is currently broken.
</p>

<p>
So I started banging around trying to fix it. Here are some of the things that
I tried.
</p>

<ul>
<li>Booting in to Windows to check the card.</li>
<li>Changing PCI slots.</li>
<li>Recompiling kernel.</li>
<li>Recompiling rt2500 driver.</li>
<li>Buying a new card.</li>
<li>(Accidentally) reinstalling the whole system.</li>
</ul>

<p>
None of which solved the problem. I would have thought with a completely clean
system running a brand new card that was verified to work in Windows would
have solved it, but I was wrong.
</p>

<p>
The failure mode was quite odd as well. No matter what I did the lights
wouldn't come on. The tools (i[fw]config) thought it was up ok, but not
associated, and showed the system trying to push packets through it, but with
no luck.
</p>

<p>
mmassonnet on #debian-xfce/freenode pointed me to a new card that uses a
different chipset/driver, the MSI PC54G3, which is supposed to work with the
rt61 driver. I have ordered one of these, and hopefully I can get it running
and forget about all of this.
</p>

<p>
[UPDATE: Just to note that the card was great until this happened, and was far
superior to what I had before (using ndiswrapper).]
</p>

