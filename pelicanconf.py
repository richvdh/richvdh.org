AUTHOR = 'richvdh'
SITENAME = "richvdh.org"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'https://getpelican.com/'),
#         ('Python.org', 'https://www.python.org/'),
#         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (
#    ('github', 'https://github.com/richvdh'),
#    ('twitter', 'https://twitter.com/richvdh'),
#)

DISPLAY_CATEGORIES_ON_MENU = False
HIDE_SIDEBAR = True

#DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'pelican-themes/pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
    'i18n_subsites',
    'simple_footnotes',
]
I18N_TEMPLATES_LANG = 'en'


MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
        'smarty' : {
            'smart_angled_quotes' : 'true'
        },
    },
    'output_format': 'html5',
}


# Tell Pelican to add files from 'extra' to the output dir
STATIC_PATHS = [
  'images',
  'extra'
]

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
}


################################################################################
#
# pelican-bootstrap3 settings
#
################################################################################

# Bootstrap theme, from https://bootswatch.com/
BOOTSTRAP_THEME= 'cerulean'
CUSTOM_CSS = 'static/css/custom.css'
