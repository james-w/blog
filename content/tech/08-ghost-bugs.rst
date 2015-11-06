Ghost Bugs
#parser reST

Please consider the following hypothetical situation. ``gnome-screensaver``
keeps crashing for people on Jaunty, which is pretty annoying, so it sends
lots of people to Launchpad to report a bug.

It's pretty quickly established by the amazing desktop team triagers that
it's actually a problem in Gtk+, so they duly reassign the bug there.

However, it's a little while before the fix is forthcoming, and it that time
many users are still getting hit by the bug, so they are still heading to
launchpad. As most of us aren't Gtk+ hackers we don't see that the issue is
there, so we go to the obvious place to report the bug, the
``gnome-screensaver`` package, and not seeing any existing reports about
the bug we file a new one.

This means that the desktop team has to spend time shovelling the bugs over
to Gtk+ and duplicating them to the first one. While we have some tools to
help with this sort of thing it would be great if we could try and avoid
it all together.

One way this could be solved in Launchpad is to leave a task open on the
``gnome-screensaver`` package, but this isn't ideal, as the bug doesn't
need to be fixed there. You could mark a ``gnome-screensaver`` bug on the
package as ``Invalid``, which would make the dupe search as you report a
bug show it, but it wouldn't show up for those that just trawled the
open ``gnome-screensaver`` bug reports looking for the crash.

My idea for something that would help in this case is `Ghost bugs`. These
are bugs that are the ghosts of a bug somewhere else. In the above case
a `ghost bug` could be created against ``gnome-screensaver`` pointing to
the Gtk+ bug. It would then show up in the bug lists, but not have a status
etc., and be somewhat "greyed out", hence the name `ghost bug`.

As the bug affects ``gnome-screensaver`` it makes sense for it to show up
against that, but as it doesn't need to be fixed there it shouldn't have
the rest of the information.

It doesn't just work for packages. See for example `launchpad bug #174539`_.
This is a bug that should be fixed in ``bzr``, but it only manifests itself
in ``bzr-builddeb``. I am keeping a task against ``bzr-builddeb`` so that
it shows up in my list to fix to have ``bzr-buiddeb`` work great, but I don't
really need a status as nothing needs to change in ``bzr-builddeb`` for it
to work.

.. _launchpad bug #174539: https://bugs.launchpad.net/bzr-builddeb/+bug/174539

With Launchpad having the concept of bug tasks this could be easily done by
adding a new status ``Ghost``, or perhaps ``Fix Elsewhere`` or something. This
would be handled differently to the other statuses, giving behaviour such as
that I described above.

Having a whole bug task may not be the right thing though. It could instead be
a separate list, similar to the list of bug tasks, but just listing the things
that should have `ghost tasks`.

Does anyone else think this would be useful? Is there prior art?
