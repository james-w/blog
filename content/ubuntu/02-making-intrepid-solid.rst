Making Intrepid Solid
#####################

:date: 2008-08-28 12:51
:slug: ubuntu/02-making-intrepid-solid

Making Intrepid Solid
=====================

With feature freeze now in effect the bulk of the big changes in Intrepid
should now be done. There will still be new features entering the archive
with the appropriate exceptions, but the rate will slow as we move forward.

Now we really need to focus on making Intrepid solid. We want to squash
as many bugs as possible, so that when we deliver the final release it is
something we can be proud of.

This is something that everyone can help with. There are plenty of ways
to help out, so there should be something for everyone.

Testing
-------

Simply running Intrepid and reporting bugs is a great start. It's still
not recommended to run it if you aren't able to fix a system that doesn't
boot, or where X doesn't start, but if you are then upgrading now will
be a great help.

You can do more than just using the system though, pick an application
and start testing all of the functionality, and report the bugs that
you find. Some bugs only show up in certain locales, with certain
hardware, or with certain combinations of packages, so try different
things and look for serious problems.

Upgrade testing is an area that is under-tested until the last minute
when floods of users upgrade. Also the easiest testing to do lots
of is upgrading pretty standard installations, but this doesn't catch
a lot of problems. So, when you are comfortable with running Intrepid
upgrade and let apport file any upgrade problems that you find. You
should also be on the lookout for unnecessary prompts that happen
while upgrading, or packages that are left broken by the upgrade.

Even if you are not happy running Intrepid yet you can still potentially
help upgrade testing, thanks to the unstoppable Michael Vogt. He
has written a tool that will clone your system in to a kvm virtual
machine, and then upgrade that. This means you can test a real
world upgrade without risk to your system. If you do this a few
times during the remaining time for Intrepid and file bugs, then
you will have a much better chance of a hassle free upgrade to the
final release. You can find more details on Michael's work `here`_.
(Not everyone has kvm capable hardware though unfortunately.)

.. _here: https://lists.ubuntu.com/archives/ubuntu-devel/2008-August/026017.html

Looking at bugs
---------------

As well as trying to find your own bugs you can look at the ones
that other people have already found. There are several important
things here.

The first is bug triage, trying to make sure that a bug report has
all the information that it needs, and trying to set an appropriate
priority. This is really important work, and we always need more
help doing it, so consider joining the bugsquad and helping out.

At this time important bugs should also be milestoned so that they
can be concentrated on for the release if possible. Deciding the
different classes of bugs here is really tricky, and there can
often be disagreements. It is important work though. If you see
a bug that should probably become release critical then work
with the bugsquad to triage it, and make sure to suggest that
it is considered for release-critical status.

Developers can help by actually trying to fix these bugs. Some
can be easy, for instance if they are known to be fixed
elsewhere. Some can be really complex, and take a lot of effort.
Fixing things from the release-critical bug list, and lists of
other important bugs is always valuable.

Doing the easy things
---------------------

There are some ways to improve the quality that are actually
fairly easy. Though there is a freeze in effect in Ubuntu there
is still loads of work going on elsewhere, and many, many bugs
being fixed elsewhere. Pulling these fixes in to Ubuntu will
improve the quality, while in theory being easier than coming
up with a fix for a bug.

We should keep an eye on upstream projects and pick up bug
fix point releases to the versions that we have. If the
project doesn't do this then look out for important fixes
going in to trunk and back-port them. If you are doing that
then it can be worthwhile looking at the versions in other
distributions that plan to release soon, and if they carry
the same version suggesting that you share the workload
of creating these point release, or at least collaborate
on fixes and share them.

Adding external bug watches in launchpad is also a great
way to help. Jorge `explained`_ this recently. This helps
easily spot when there is a bug fix that we could pull in.
When there is they will appear on `harvest`_

.. _explained: http://stompbox.typepad.com/blog/2008/08/feeding-the-har.html
.. _harvest: http://daniel.holba.ch/harvest/

Harvest (now with a new look) is another easy way to do
things. It lists opportunities to fix things that should
be fairly easy, such as bugs fixed elsewhere, or bugs with
patches attached.

Making Intrepid+1 rock
======================

In parallel with all the above now is the time to start thinking
about what you want to achieve in the next cycle. If any of
that requires changes to an upstream then speaking to them
early can be a good idea, as you can get their feedback and see
how it fits in to their plan. I'm sure everyone has loads of
ideas, and a bit of preparation now can help you hit the ground
running in the next cycle.

