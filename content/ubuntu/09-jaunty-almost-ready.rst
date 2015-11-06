Jaunty's almost ready
#parser reST

Jaunty just froze a little bit more, with the last few normal uploads being
done. From here on in it's mainly about getting the CDs perfect for release,
which will hopefully go smoothly.

Over the last few days there have been a number of people working on Universe
to get it in to the best shape we could in the remaining time. We did a
pretty good job of it too, towards the end we were scavenging around for any
more fixes that were ready to upload. As always, with more people we could
have done more, but it seemed to be a very smooth landing this time.

The sponsorship queue is virtually all things that were not appropriate for
Jaunty, with just a couple of desirable fixes not making the cut (we'll work
to have those in jaunty-updates ASAP). In addition to that, NBS was clear,
meaning that there were no outstanding library transitions or similar,
and there are very few uninstallables. Obviously we would want all of these
numbers to be zero, but you can't have that with a time-based release
schedule. Unfortunately the FTBFS list is rather long (mainly due to
toolchain changes), but it's generally infrequently updated packages on
there, which will tend to be of less interest.

The MOTUs also did a fantastic job of the python 2.6 transition, which was
a huge job, and a compressed timeframe to do it in. Unfortunately there
are going to be some issues with the change in the default python for
some time to come, but given the state of python a couple of months ago
this is a great acheivement.

Also, I'll make special mention of the Mono 2.0 transition. Co-ordinated
by Jo Shields, and thanks to a lot of people on both the Debian and Ubuntu
sides, this was completed with very little fuss. It was a great example
of co-ordinating work on a large number of packages, and of collaboration
between Debian and Ubuntu. I also think that it showed some of the advantages
of the Ubuntu method of development over the Debian one, but the
shared work trumps that.

If you are reading this thinking "You might think you did a good job,
but what about this bug that I provided a patch for 3 months ago,
why didn't you fix that?" then all I can really do is point you to
the `sponsorship process`_. Yes, it sucks that not knowing about this
cost you, but reviewing every bug with an attachment tagged "patch"
is currently a little out of our reach. I'm always looking for ways
to improve this, and I hope one day we can do that, but in the meantime
using the sponsorship process will help get your patch included.

.. _sponsorship process: https://wiki.ubuntu.com/SponsorshipProcess
