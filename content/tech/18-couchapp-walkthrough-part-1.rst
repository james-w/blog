Couchapp Walkthrough - Part 1
#parser reST

Couchapps are a particular way of using couchdb that allow you to
serve web applications directly from the database. These applications generate
HTML and javascript to present data from couchdb to the user,
and then update the database and the UI based on their actions.

Of course there are plenty of frameworks out there that do this sort of thing,
and more and more of them are adding couchdb support. What
makes couchapps particularly interesting are two things. Firstly, the
ease with which they can be developed and deployed. As they are served
directly from couchdb they require little infrastructure, and the
couchapp tool allows for a rapid iteration. In addition, the conveniences
that are provided mean that simple things can be done very quickly with
little code.

The other thing that makes couchapps attractive is that they live inside
the database. This means that the code lives alongside the data, and will
travel with it as it is replicated. This means that you can easily have
an app that you have fast, local access to on your desktop, while
at the same time replicating to a server so that you can access the same
data from your phone while you are out. Again, this doesn't require
couchapps, and they won't be suitable for all needs, but they are certainly
an interesting idea.

You can read more about couchapps at `http://couchapp.org`_.

.. _http://couchapp.org: http://couchapp.org

Intrigued by couchapps I set out to play with them over a weekend. Unfortunately
the documentation is rather lacking currently, so I wouldn't recommend experimenting
yourself if you are not happy digging around for answers, and sometimes
not finding them outside the code. In order to
go a little way to rectifying this, I intend to write a few posts about
the things I wish I had known when I started out. I found everything to be
a little strange at first, and it wasn't even clear where the entry point
of a couchapp was for instance. Hopefully these posts will be found using
google by others who are struggling in a similar way.

Architecture
------------

Firstly something about the pieces that make up a couchapp (or at least those
that the tool and documentation recommend,) and the way that they all fit together.

At the core is the couchdb database itself. It is a collection of "documents",
each of which can have attachments. Some of these documents are known as
"design documents," and they start with a prefix of "_design." Design
documents can have "view" functions, and various other special fields
that can be used to query or manipulate other documents.

A couchapp is a design document with an attachment, usually called index.html.
These attachments are served directly by couchdb and can be accessed at a
known URL. You can put anything you like in that html file, and you could
just have a static page if you wanted. Usually however though it is is
an HTML page that uses javascript in order to display the results
of queries on the database. The user will then access the attachment on
the design document, and will interact with the resulting page.

In theory you can do anything you like in that page, but it is usual
to make use of standard tools in order to query the database and
provide information and opportunity for interaction to the user.

The first standard tool is jQuery, with a couple of plugins for
working with couchdb and couchapps specifically. These allow for
querying views in the database and acting on the results, retrieving
and updating documents, and plenty more.

In addition the couchapp tool sets you up with another jQuery
plugin called "evently", which is a way to structure interactions
with jQuery, and change the page based on various events. I will
go in to more detail about how evently works in a later post.

In addition to all the client-side tools for interacting with the
database, it is also possible to make use of couchdb features such
as shows, lists, update handlers validation functions in order to move
some of the processing server-side. This is useful for various reasons,
including being more accessible, allowing search engines to index the
content, and not having to trust the client not to take malicious
actions.

The two approaches can be combined, and you can prototype with the
client-side tools, and then move some of the work to the server-side
facilities later.

Stay tuned for more on how a simple couchapp generates content based
on what is in the db.
