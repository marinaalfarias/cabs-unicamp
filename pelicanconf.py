#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Bernardo Sayão'
SITENAME = 'Centro Acadêmico Bernardo Sayão'
SITEURL = 'cabs-unicamp.gitlab.io'
OUTPUT_PATH = 'public/'
PATH = 'content'
THEME = 'theme'
LOGO = '/theme/images/logo.svg'
FAVICON = '/favicon.ico'
BACKGROUND = '/theme/images/background.jpg'

TIMEZONE = 'America/Sao_Paulo'
LOCALE = 'pt_BR.utf8'
DEFAULT_LANG = 'pt-BR'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%d/%m/%Y'


PAGE_PATHS = ['pages',]
ARTICLE_PATHS = ['articles',]
USE_FOLDER_AS_CATEGORY=True

STATIC_PATHS = [
    'images',
    'extra',
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
MAINMENU = (('Inicio', ''),
         ('Sobre', 'sobre'),
         ('Contato', 'contato'),
         )

MENUITEMS = (('Inicio', '/'),
         )

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

CATEGORY_URL = '{slug}.html'
CATEGORY_SAVE_AS = '{slug}.html'

DEFAULT_PAGINATION = 5
DEFAULT_ORPHANS = 0


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False
