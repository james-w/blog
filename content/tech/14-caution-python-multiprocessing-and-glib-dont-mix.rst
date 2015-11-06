Caution: python-multiprocessing, threads and glib don't mix
###########################################################

:date: 2010-04-08 13:01
:slug: tech/14-caution-python-multiprocessing-and-glib-dont-mix

If you don't want to read this article, then just steer clear of
python-multiprocessing, threads and glib in the same application. Let me
explain why.

There's a rather `famous bug`_ in `Gwibber`_ in Ubuntu Lucid, where
a gwibber-service process will start taking 100% of the CPU time
of one of your cores if it can. While looking in to why this bug
happened I learnt a lot about how multiprocessing and GLib work,
and wanted to record some of this so that others may avoid the
bear traps.

.. _famous bug: https://bugs.edge.launchpad.net/ubuntu/+source/gwibber/+bug/554005
.. _Gwibber: https://launchpad.net/gwibber

Python's `multiprocessing module`_ is a nice module to allow you to
easily run some code in a subprocess, to get around the restriction of
the GIL for example. It makes it really easy to run a particular function
in a subprocess, which is a step up from what you had to do before it
existed. However, when using it you should be aware how the way it works
can interact with the rest of your app, because there are some possible
nasties lurking there.

.. _multiprocessing module: http://docs.python.org/library/multiprocessing.html

`GLib` is a set of building blocks for apps, most notably used by GTK+.
It provides an object system, a mainloop and lots more besides. What we are
most interested here is the mainloop, signals, and thread integration that
it provides.

.. _GLib: http://library.gnome.org/devel/glib/

Let's start the explanation by looking at how multiprocessing does its thing.
When you start a subprocess using multiprocessing.Process, or something that
uses it, it causes a fork(2), which starts a new process with a copy of the
programs current memory, with some exceptions. This is really nice for
multiprocessing, as you can just run any code from that program in the
subprocess and pass the result back without too much difficulty.

The problems occur because there isn't an exec(3) to accompany the fork(2).
This is what makes multiprocessing so easy to use, but doesn't insert a clean
process boundary between the processes. Most notably for this example, it
means the child inherits the file descriptors of the parent (critically even
those marked FD_CLOEXEC).

The other piece to this puzzle is how the GLib mainloop communicates
between threads. It requires some mechanism where one thread can alert
another that something of interest happened. To do this when you tell
GLib that you will be using threads in your app by calling g_thread_init
(gobject.threads_init() in Python) then it will create a pipe for use by
glib to alert other threads.  It also creates a watcher thread that
polls one end of this pipe so that it can act when a thread wishes to
pass something on to the mainloop.

The final part of the puzzle is what your app does in a subprocess with
mutliprocessing. If you purely do something such as number crunching
then you won't have any issues. If however you use some glib functions
that will cause the child to communicate with the mainloop then you
will see problems.

As the child inherits the file descriptors of the parent it will use the
same pipe for communication. Therefore if a function in the child writes
to this pipe then it can put the parent in to a confused state. What
happens in gwibber is that it uses some gnome-keyring functions and that
puts the parent in to a state where the watcher thread created by
g_thread_init busy-polls on the pipe, taking up as much CPU time as it can
get from one core.

In summary, you will see issues if you use python-multiprocessing from
a thread and use some glib functions in the children.

There are some ways to fix this, but no silver bullet:

  * Don't use threads, just use multiprocessing. However, you can't
    communicate with glib signals between subprocesses, and there's
    no equivalent built in to multiprocessing.
  * Don't use glib functions from the children.
  * Don't use multiprocessing to run the children, use exec(3) a script
    that does what you want, but this isn't as flexible or as
    convenient.

It may be possible to use the support for different GMainContexts for
different threads to work around this, but:

  * You can't access this from Python, and
  * I'm not sure that every library you use will correctly implement it,
    and so you may still get issues.

Note that none of the parties here are doing anything particularly
wrong, it's a bad interaction caused by some decisions that are known to
cause issues with concurrency. I also think there are issues when using
DBus from multiprocessing children, but I haven't thoroughly
investigated that. I'm not entirely sure why the multiprocessing child
seems to have to be run from a non-main thread in the parent to trigger
this, any insight would be welcome. You can find a small script to
reproduce the problem `here`_.

.. _here: http://jameswestby.net/scratch/multiprocessing_bug.py

Or, to put it another way, global state bad for concurrency.

