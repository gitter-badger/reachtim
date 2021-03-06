#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tim Arnold'
SITENAME = u'ReachTim'
SITESUBTITLE = 'Python, LaTeX, and XML: coding together.'
SITEURL = 'http://reachtim.com'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'
PATH = 'content'

OUTPUT_PATH = 'reachtim/'
ARTICLE_PATHS = ['articles',]
STATIC_PATHS = ['images', 'extra',]

EXTRA_PATH_METADATA = {
    'extra/404.html': {'path': '404.html'},
    'extra/403.html': {'path': '403.html'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/.htaccess': {'path':  '.htaccess'},
    'extra/crossdomain.xml': {'path':  'crossdomain.xml'},
    'extra/favicon.ico': {'path':  'favicon.ico'},
}

ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

THEME = '../themes/zurb-F5-basic'
PLUGIN_PATHS=['../plugins',]
PLUGINS = [
	'neighbors',
    'pelican_fontawesome',
    'pelican_gist',
	'render_math',
	'sitemap',
	]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

DISQUS_SITENAME = 'reachtim'
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

LINKS = (
         ('Planet Python', 'http://planet.python.org/'),
         ('CTAN', 'http://ctan.org/'),
         ('LaTeX Community', 'http://latex-community.org'),
         ('DocBook', 'http://www.docbook.org/'),
         ('DocBook XSL', 'http://www.sagehill.net/'),
         )
SOCIAL = (
          ('Github', 'https://github.com/tiarno'),
          ('Gists', 'https://gist.github.com/tiarno/'),
          ('LinkedIn', 'https://www.linkedin.com/in/jtimarnold'),
         )

DEFAULT_PAGINATION = 10

TYPOGRIFY = True
MD_EXTENSIONS= [
	'codehilite(css_class=highlight)',
	'extra',
    'toc',
	]
