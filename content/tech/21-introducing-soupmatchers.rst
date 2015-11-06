Introducing soupmatchers
#parser reST

jml `just announced testtools 0.9.8`_ and in it mentioned the `soupmatchers`_
project that I started. Given that I haven't talked about it here before, I wanted to
do a post to introduce it, and explain some of the rationale behind it.

.. _just announced testtools 0.9.8: http://code.mumak.net/2010/12/testtools-098-released.html
.. _soupmatchers: http://launchpad.net/soupmatchers

soupmatchers is a library for unit testing HTML, allowing you to assert that certain things
are present or not within an HTML string. Asserting this based on substring matching is going
to be too fragile to be usable, and so soupmatchers works on a parsed representation of the HTML.
It uses the wonderful `BeautifulSoup`_ library for parsing the HTML, and allows you to assert
the presence or not of tags based on the attributes that you care about.

.. _BeautifulSoup: http://www.crummy.com/software/BeautifulSoup/

::

    self.assertThat(some_html,
                    HTMLContains(Tag('testtools link', 'a',
                    attrs={'href': 'https://launchpad.net/testtools'})))

You can see more examples in `the README`_.

.. _the README: http://bazaar.launchpad.net/~soupmatchers-dev/soupmatchers/trunk/annotate/head:/README

Basing this on the testtools matchers frameworks allows you to do this in a semi-declarative way.
I think there is a lot of potential here to improve your unit tests. For instance you can
start to build a suite of matchers tailored to talking about the HTML that your application outputs.
You can have matchers that match areas of the page, and then talk about other elements relative to
them ("This link is placed within the sidebar"). One thing that particularly interests me is to create
a class hierarchy that allows you test particular things across your application. For instance,
you could have an ExternalLink class that asserts that a particular class is set on all of your
external links. Assuming that you use this at the appropriate places in your tests then you will know that the
style that is applied to class will be on all external links. Should you wish to change the way that
external links are represented in the HTML you can change the one class and your tests should tell you
all the places that the code has to be updated.

Please go ahead and try the library and `let me know`_ how it could be improved.

.. _let me know: https://bugs.launchpad.net/soupmatchers/+filebug
