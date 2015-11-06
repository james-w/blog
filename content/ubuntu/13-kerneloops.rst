Kerneloops enabled by default in Karmic
#parser reST

One of the new things that is going to be in karmic is that
the kerneloops daemon will be installed and running by default.
This tool, created by Arjan van de Ven, watches the kernel logs for
problems. It has a companion service, `kerneloops.org`_ which aggregates
reports of these problems, and can sort by kernel version and the like.
This allows kernel developers to spot the most commonly encountered
problems, areas of the code which are prone to bugs etc. When the
kerneloops daemon catches a problem it allows you to send the
problem to kerneloops.org.

.. _kerneloops.org: http://kerneloops.org/

We however, are not using the applet that comes with kerneloops to do
this, we are making use of the brilliant Apport. There are a couple
of reasons for this. We also want to make it easy for you to report
these issues as bugs to Launchpad, and we don't want to prompt you
with two different interfaces to do that.

The changes mean that if your machine has a kernel issue you will
get an apport prompt as usual. As well as asking if you would like
to report the problem to Launchpad like it does for other crashes
it will ask if you would also like to report it to kerneloops.org.
Passing the information through apport means that it can also be used
on servers as well without running X.

Hopefully you will never see this improvement, but it's now going to
be there for when those bugs do creep in.
