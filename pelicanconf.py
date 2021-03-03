#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Bernardo Sayão'
SITENAME = 'Centro Acadêmico Bernardo Sayão'
SITEURL = 'cabs-unicamp.gitlab.io'
SITEDESCRIPTION = 'Página do CABS, centro acadêmico do curso de Engenharia Elétrica da Universidade Estadual de Campinas (Unicamp)'
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

PV_LIST = [
       ('Ingresso 2020', '/pv/ingresso_2020.png', '/pv/ingresso_2020.pdf'),
       ('Ingresso 2019', '/pv/ingresso_2019.png', '/pv/ingresso_2019.pdf'),
       ('6 Edicao 2018', '/pv/6aEdicao2018.png', '/pv/6aEdicao2018.pdf'),
       ('Ingresso 2018', '/pv/ingresso_2018.png', '/pv/ingresso_2018.pdf'),
       ('5 Edicao 2017', '/pv/5aEdicao2017.png', '/pv/5aEdicao2017.pdf'),
       ('4 Edicao 2017', '/pv/4aEdicao2017.png', '/pv/6aEdicao2017.pdf'),
       ('3 edicao 2014', '/pv/3aEdicao2014.png', '/pv/3aEdicao2014.pdf'),
       ('2 edicao 2014', '/pv/2aEdicao2014.png', '/pv/2aEdicao2014.pdf'),
       ('1 edicao 2013', '/pv/1aEdicao2013.png', '/pv/1aEdicao2013.pdf'),
        ]

STATIC_PATHS = [
    'images',
    'extra',
    'admin',
    'pv'
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'admin/config.yml': {'path': 'admin/config.yml'},
}

TEMPLATE_PAGES = {
    'admin/index.html': {'path': 'admin/index.html'},
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (('blog', '/'),
         )

ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

CATEGORY_URL = '{slug}.html'
CATEGORY_SAVE_AS = '{slug}.html'

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_PAGINATION = 5
DEFAULT_ORPHANS = 0


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False
