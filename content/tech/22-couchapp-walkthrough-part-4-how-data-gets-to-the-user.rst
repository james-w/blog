Couchapp Walkthrough: Part 4: How data gets to the user
#parser reST

This was the confusing part when I first ran ``couchapp`` to create a new app,
I couldn't really see where the "entry point" of the app was. In the hope that
it might help someone else I'm going to present a quick overview of the default
setup.

``index.html``
--------------

The ``index.html`` page is a static attachement, and the user starts by requesting
it with their browser.

It has some small amount of static HTML, part of which creates a ``div`` for the
javascript to put the data in.

Either inline, or in an included file, there is a small bit of javascript that will
initialise the couchapp.

By default this will use the ``div`` with the id ``items``, and will attach an
``evently`` widget to it.

``evently``
-----------

The ``evently`` widget that is attached will then either have an ``_init`` event,
or a ``_changes`` event, either of which will be immediately run by ``evently``.

This event will usually make a couchdb query to get data to transform to HTML and
present to the user (see `part three` for how this works.)

.. _part three: http://jameswestby.net/weblog/tech/20-couchapp-walkthrough-part-3-evently.html

Once that data has been displayed the user any combination of ``evently`` widgets or
javascript can be used to make further queries and build an app that works however
you like.

Previous installments
---------------------

See `part one`_, `part two`_, and `part three.`_

.. _part one: http://jameswestby.net/weblog/tech/18-couchapp-walkthrough-part-1.html
.. _part two: http://jameswestby.net/weblog/tech/19-couchapp-walkthrough-part-2-the-couchapp-tool.html
.. _part three.: http://jameswestby.net/weblog/tech/20-couchapp-walkthrough-part-3-evently.html
