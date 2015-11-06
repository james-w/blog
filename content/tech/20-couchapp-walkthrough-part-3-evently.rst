Couchapp Walkthrough: Part 3: Evently
#parser reST

[ Apologies to those that saw this half-finished when I published
rather than saving a draft ]

This is the part that it took me a long time to understand: how the different
parts of the default couchapp collaborate to present data to the user.

In this post I'm just going to deal with client-side couchapps using the
default technologies. As explained in the previous post you can use any
combination of HTML and javascript in a couchapp, and you can also do some
of the work server-side in couchdb. However, I'm going to explain what
the couchapp tool gives you when you create a new project, as that is
where you are likely to be starting, and once you understand that you
can choose where to deviate from that model.

jQuery events
-------------

Our first detour is in to a little bit of background, the excellent
javascript libarary that is heavily used in couchapps.

jQuery allows for events on elements in the DOM. There are standard
events, such as "click" and "submit", but you are free to define your
own.

These events are given a name, and you can then "trigger" them, and
bind handlers to act when they are triggered.

By building up events from low level ones such as "click", to more-complex
and app-specific ones such as "item purchased", you can break down
your code in to smaller chunks, and have different parts of the page
react to the same event, such as having the "buy" link disappear from
the item that the user just bought, as well as having the total of
the shopping cart update.

Events can also have data, or arguments, that travels with them. For instance
the "item purchased" event could have the item that was purchased as the
data, so that handlers can make use of it when they run.

evently
-------

Now that we know something about jQuery events, we can look at something
built on top of them, the "evently" library. This is a layer on top of
jQuery that allows you build up your app from pieces that have a specific
function, and communicate through events.

An evently "widget" can be bound to an element (or several elements if
you want). The widget is a bunch of event handlers which can do anything
you like, but have some conveniences built in for fetching data and
updating the page based on the result.

When an event is triggered the handler you defined is run. If it is
a simple javascript function then that function is run, and can do
anything you like.

::

    {click: function() {
            alert("You clicked!");
        }
    }

Often though you want to update the element based on the action. evently
has built in support for the "mustache" templating language, and if you
specify a template in that syntax it will replace the current HTML
of the element that it is attached to with the result of rendering
that template.

::

    {click: 
        {
            mustache: "<div>You clicked!</div>"
        }
    }

Which will put "You clicked!" in to the page instead of in an alert. What
if you don't want to replace the current content, and just want to append
another line? For that use the "render" option.

::

    {click: 
        {
            mustache: "<div>You clicked!</div>",
            render: "append"
        }
    }

Which would put another "You clicked!" on the page every time you click.
As well as "append" there is also "prepend", or really any jQuery method
that you want to call.

Simply rendering a static template isn't going to be very useful though,
usually you want something dynamic. For that use the "data" option,
which can just be an object if you want, but that's still not going to
be very dynamic either, so it can be a function that returns an object.

::

    {click: 
        {
            data: function(e) {
                return {name, "Bob"};
            },
            mustache: "<div>Hi {{name}}!</div>"
        }
    }

The data function gets passed the event object from jQuery (so you
can e.g. get the target of the event), and any data for the event
too (so it could see what item you just bought).

That's all well and good, but it doesn't help us get data from couchdb
in to the page. For that we need the opportunity to make a request
to couchdb. We could just fall back to using one function to handle
the event, but then we lose the integration with mustache. Therefore
there is an "async" key that allows us to make an AJAX request
and then use mustache on the result.

::

    {click: 
        {
            async: function(callback) {
                /* some code that does an async request, and then calls callback with the result */
            },
            data: function(resp) {
                /* Some code that processes the data from the async function to ready it for the template */
            },
            mustache: "A tempate that will be rendered with the result of the data function"
        }
    }

Now, writing an async method to query a couchdb view is so common in couchapps that
eventy has special support for it. The ``query`` key can either be a json
structure that specifies a view and the arguments to it, or a function that
returns such a structure based on things such as the query string in the URL.

There are two further functions that you will find helpful from time to time. The
first is ``before`` that allows you to run some code before the rest of the process
starts, and may do something such as trigger another event. The other is its partner
``after``, which can do much the same things as ``before``, but can also do things
such as modify the HTML that is output.

Lastly there is another thing that can be done with the HTML that is output,
specified with they ``selectors`` key. This allows you to perform an action
on particular parts of the html. The keys of this structure are jQuery
selectors that specify which elements the function will be applied to. For
instance you can do something with all the divs in the output, or all the
spans with a certain class, or the form with a particular id.

What you can do to those elements is basically unlimited, as you can run
arbitrary javascript. However, there is built in support for specifying
an evently widget, which will automatically be bound to each element
that matches the selector. This nesting is one of the most powerful and
useful features of evently, and one you should generally be using often.
I will probably talk more about what nested widgets are useful for later.

Special evently events
----------------------

evently has two special events. The first of these is ``_init``. This
event is triggered when the widget is created. This means you can
dynamically pre-populate the element, or at least keep the inital
state of the element with the rest of your code, rather than putting
some in the HTML file and the rest in evently code.

The other special event is tied to couchdb, and is the ``_changes``
event, and is triggered whenever the database that the couchapp is
in changes. This means that you can have elements on the page that
dynamically update whenever the database changes, whether that is
through user action, another user doing something, external scripts,
or couchdb replication. This makes it very easy to write "live"
pages that show updates without refreshes, and is very useful for
some applications.

Currently ``_changes`` doesn't receive the modified documents, so
it is normally just used to make another request to get the updated
information, whether that be through ``async`` or ``view``. If
you wish to get the modified documents in order to update the page
directly and reduce requests then you can write some custom code
to do this.

Conclusion
----------

As you have seen, evently is just a thin layer on top of jQuery concepts
such as events and asynchronous events, with some conveniences for
templating and interacting with couchdb.

This combination is well suited to the needs of at least simple
and moderately complex couchapps, while still being very powerful,
and allowing you to fall back to custom javascript at any point.

You can find more about evently at `the couchapp site.`_

.. _the couchapp site.: http://couchapp.org/page/evently

See `part one`_ and `part two.`_

.. _part one: http://jameswestby.net/weblog/tech/18-couchapp-walkthrough-part-1.html
.. _part two.: http://jameswestby.net/weblog/tech/19-couchapp-walkthrough-part-2-the-couchapp-tool.html
