import os
from datetime import datetime
from calendar import month_name
# If your site is available via HTTPS, make sure SITEURL begins with https://
RELATIVE_URLS = False

AUTHOR = 'offen'
SITENAME = 'offen'
PATH = 'content'
TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'en'

BUILD_DATE = '{} {}'.format(month_name[datetime.today().month], datetime.today().year)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SITEURL = 'http://localhost:8000'

# pagination
DEFAULT_PAGINATION = False

THEME = './theme'

# Delete the output directory before generating new files.
DELETE_OUTPUT_DIRECTORY = True

DIRECT_TEMPLATES = ['sitemap', 'archives']

# dont create following standard pages
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''

ARCHIVES_SAVE_AS = 'blog/index.html'
SITEMAP_SAVE_AS = 'sitemap.xml'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['decorate_content', 'assets']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.fenced_code': {},
    },
    'output_format': 'html5',
}

DECORATE_CONTENT = {
    '[data-button]': ['w-100', 'w-auto-ns', 'tc', 'tl-ns', 'dib', 'mt3', 'ph4', 'pv2', 'b--solid', 'bw2'],
    '[data-button-mb5]': ['w-100', 'w-auto-ns', 'tc', 'tl-ns', 'dib', 'mt3', 'mb5', 'ph4', 'pv2', 'b--solid', 'bw2'],
    '[data-button="outline"]': ['b--gray', 'gray'],
    '[data-button="full"]': ['cclr-brd-black-mid', 'white', 'cclr-bg-black-mid'],
    '[data-button-mb5="full"]': ['cclr-brd-black-mid', 'white', 'cclr-bg-black-mid'],
    'a': ['link', 'b', 'dim'],
    'a:not([data-button])': ['gray'],
    'h5 a': ['normal', 'moon-gray'],
    'h1': ['f2', 'normal', 'lh-title', 'mt4', 'ma0', 'mb3', 'light-silver'],
    'h2': ['f25', 'normal', 'lh-title', 'mt4', 'ma0', 'mb3', 'light-silver'],
    'h3': ['f5', 'normal', 'mt5', 'ma0', 'mb3', '.cclr-fnt-black-mid'],
    'h4': ['f5', 'b', 'mt4', 'ma0', 'mb1'], # text over button
    'h5': ['f7', 'normal', 'ma0', 'nt5', 'mb5', 'moon-gray'], # image credits
    'h6': ['f5', 'lh-solid', 'normal', 'ma0', 'mb3', 'light-silver'], # date
    'p': ['ma0', 'pb3'],
    'blockquote': ['f5', 'i', 'ma0', 'ml4-ns', 'ml3'],
    'hr': ['mt5', 'mb3', 'b--black-05'],
}

DOCS_URL = 'https://docs.offen.dev'
GITHUB_REPO = 'https://github.com/offen/offen'
CONTACT_EMAIL = 'hioffen@posteo.de'
PGP_KEY_FILE = '74B041E23DB29D552644CEB1B18C633D6967FE3F.asc'
PATREON_URL = 'https://www.patreon.com/offen'
LINKEDIN_URL = 'https://www.linkedin.com/company/hioffen'
TWITTER_URL = 'https://twitter.com/hioffen'
RELEASE_DIRECT_URL = 'https://get.offen.dev'
DOCKER_DIRECT_URL = 'https://hub.docker.com/r/offen/offen'
HEROKU_DIRECT_URL = 'https://heroku.com/deploy?template=https://github.com/offen/heroku/tree/master'
OFFEN_AUDITORIUM_URL = 'https://analytics.offen.dev/auditorium'
DOCS_GETSTARTED_URL = 'https://docs.offen.dev/running-offen/'
DOCS_TRYDEMO_URL = 'https://docs.offen.dev/running-offen/test-drive/'

OFFEN_ACCOUNT_ID = os.environ.get('OFFEN_ACCOUNT_ID', None)
