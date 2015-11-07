#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'James Westby'
SITENAME = u'James Westby'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/jdwestby'),
          ('GitHub', 'https://github.com/james-w/'),
          ('Launchpad', 'https://launchpad.net/~james-w', 'pencil'),
        )

DEFAULT_PAGINATION = 20

THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'readable'

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_PAGES_ON_MENU = True

CC_LICENSE = "CC-BY-SA"

TWITTER_CARDS = True
TWITTER_USERNAME = 'jdwestby'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
