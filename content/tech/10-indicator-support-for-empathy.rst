Indicator support for Empathy
#############################

:date: 2009-04-06 00:11
:slug: tech/10-indicator-support-for-empathy

As well as the new notification bubbles, jaunty now has something called
the "indicator-applet", or various other names. If you are running Jaunty
you may have seen it as an envelope in your panel. Not much is taking
advantage of it yet, with only Evolution and Pidgin having the necessary
support until recently.

The purpose of this applet is to give you access to messages that are waiting
for you, regardless of the source. You can see some of Ted's early `sketches
on the idea`_, or the `early draft of the spec`_ for some information. Having
this place gives you one place to look to respond to a message you received,
and is part of the strategy to solve the issues caused by having notifications
without actions. It also allows you to launch the main windows of the
applications so you don't need to have an icon for each in the notification
area.

.. _sketches on the idea: http://gould.cx/ted/blog/Where_are_my_messages_
.. _early draft of the spec: https://wiki.ubuntu.com/MessagingMenu

As I don't use pidgin the only thing taking advantage of the menu was evolution,
so I went to find which of the other apps I use had support. I first grabbed
a more recent version of gwibber which had support, and sent a quick merge
request to improve the support. There was little else I could do there though,
as Ryan had done a great job already, and all I had to do was hook up a callback
so that gwibber would open when you clicked on a message you received from
someone.

I then moved on to Empathy, and found a `bug requesting support be added`_.
I decided to relax this weekend by working on something completely different
and trying to add this support.

.. _bug requesting support be added: http://bugzilla.gnome.org/show_bug.cgi?id=574744

I found the libindicate API easy to work with, though it is un-documented
currently there is not too much too it, and it has quite some similarity with
libnotify. After finding my way around the empathy internals, learning more
about gtk+ and encountering a `bug in libindicate`_ that I spent some time
investigating I had something mostly working. It's not ready to merge yet,
but it is most of the way there, and covers the most common cases.

.. _bug in libindicate: https://bugs.launchpad.net/indicator-applet/+bug/351537

You can see a `quick video of the interaction`_, which shows the concept
behind the menu as well. (Yes, I am talking to myself in that video, as
Ted said, working on IM apps can be quite lonely as you continually send
yourself messages).

.. _quick video of the interaction: http://jameswestby.net/images/empathy-indicator.ogv
