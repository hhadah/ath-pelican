#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site development flag
developing_site = True

#-------------------
# Site information
#-------------------
AUTHOR = 'Andrew Heiss'
SITENAME = 'Andrew Heiss'
MINIBIO = 'Scholar, developer, and designer'

SITEURL = ''

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

DEFAULT_DATE_FORMAT = '%A, %B %-d, %Y'

TYPOGRIFY = True  # Nice typographic things


#----------------
# Site building
#----------------
# Theme
THEME = '/Users/andrew/Development/•Pelican/themes/athpelican-theme'

# Folder where everything lives
PATH = 'content'

# Structure of output folder
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

INDEX_SAVE_AS = 'blog/index.html'

YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'

# Get rid of author pages (since I'm the only author) and the archives page
# (since I'm doing that manually)
DIRECT_TEMPLATES = ('index', 'categories')

# Include source files, just for fun
OUTPUT_SOURCES = True
OUTPUT_SOURCES_EXTENSION = '.txt'

# Ordering
PAGE_ORDER_BY = 'date'
ARTICLE_ORDER_BY = 'date'


#----------
# Plugins
#----------
PLUGIN_PATHS = ['/Users/andrew/Development/•Pelican/pelican-plugins']
PLUGINS = ['pandoc_reader', 'collate_content', 'sitemap', 'dateish', 'sort_tags']

# Pandoc settings
PANDOC_ARGS = [
    '--smart',
    '--base-header-level=2'
]

# collate_content settings
# CATEGORIES_TO_COLLATE = ['category-of-interest', 'another-cool-category']

# Sitemap settings
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

# dateish settings
# DATEISH_PROPERTIES = ['created_date', 'idea_date']


# Feed generation
FEED_ALL_ATOM = None if developing_site else None
CATEGORY_FEED_ATOM = None if developing_site else None
TRANSLATION_FEED_ATOM = None if developing_site else None
AUTHOR_FEED_ATOM = None if developing_site else None
AUTHOR_FEED_RSS = None if developing_site else None

# Cache
LOAD_CONTENT_CACHE = False if developing_site else True


#-------------
# Site items
#-------------
MENUITEMS = [('About', '/about/'), ('CV', '#'), ('Blog', '/blog/'),
             ('Research', '/research/'), ('Teaching', '/teaching/'),
             ('Resources', '#'), ('Other projects', '#')]

SOCIAL = [('E-mail', 'mailto:andrew@andrewheiss.com', 'fa-envelope-square'),
          ('Heissatopia (family blog)', 'http://www.heissatopia.com', 'fa-smile-o'),
          ('Facebook', 'https://www.facebook.com/andrewheiss', 'fa-facebook-square'),
          ('Twitter', 'https://twitter.com/andrewheiss', 'fa-twitter-square'),
          ('GitHub', 'https://github.com/andrewheiss', 'fa-github-square'),
          ('StackOverflow', 'https://stackoverflow.com/users/120898/andrew', 'fa-stack-overflow'),
          ('LinkedIn', 'https://www.linkedin.com/in/andrewheiss', 'fa-linkedin-square'),
          ('Google+', 'https://plus.google.com/+AndrewHeiss', 'fa-google-plus-square'),
          ('Academia.edu', 'https://duke.academia.edu/AndrewHeiss', 'fa-graduation-cap')]


#----------------
# Jinja filters
#----------------
import jinja2
import markdown

# Remove <p>s surrounding Markdown output
def md_single_line(text):
    p = '<p>'
    np = '</p>'
    md = markdown.markdown(text)
    if md.startswith(p) and md.endswith(np):
        md = md[len(p):-len(np)]
    return jinja2.Markup(md)

def md(text):
    return jinja2.Markup(markdown.markdown(text))

JINJA_FILTERS = {'md_single_line': md_single_line,
                 'md': md}