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

DECORATE_CONTENT = {
    '[data-button]': ['w-100', 'w-auto-ns', 'tc', 'tl-ns', 'dib', 'mt3', 'ph4', 'pv2', 'b--solid', 'bw2'],
    '[data-button-mb5]': ['w-100', 'w-auto-ns', 'tc', 'tl-ns', 'dib', 'mt3', 'mb5', 'ph4', 'pv2', 'b--solid', 'bw2'],
    '[data-button="yellow"]': ['brd-cclr-mid-yellow', 'fnt-cclr-mid-yellow'],
    '[data-button="black"]': ['brd-cclr-mid-black', 'fnt-cclr-mid-black'],
    '[data-button-mb5="black"]': ['brd-cclr-mid-black', 'fnt-cclr-mid-black'],
    'a': ['link', 'b', 'dim'],
    'a:not([data-button])': ['gray'],
    'h1': ['f2', 'normal', 'lh-title', 'mt4', 'ma0', 'mb3', 'light-silver'],
    'h2': ['f25', 'normal', 'lh-title', 'mt4', 'ma0', 'mb3', 'light-silver'],
    'h3': ['f5', 'normal', 'mt4', 'ma0', 'mb3', 'fnt-cclr-mid-black'],
    'h4': ['f5', 'normal', 'mt4', 'ma0', 'mb3'],
    'h5': ['f5', 'b', 'mt4', 'ma0', 'mb1'], # text over button
    'h6': ['f5', 'lh-solid', 'normal', 'ma0', 'mb3', 'light-silver'], # date
    'p': ['ma0', 'pb3'],
    'blockquote': ['f5', 'i', 'ma0', 'ml4-ns', 'ml3'],
    'hr': ['mt5', 'mb3', 'b--black-05'],
    '[spacer-4]': ['ma0', 'mb4']
}

GITHUB_ORG = 'https://github.com/offen'
CONTACT_EMAIL = 'hioffen@posteo.de'
GPG_KEY_FILE = '74B041E23DB29D552644CEB1B18C633D6967FE3F.asc'
PATREON_URL = 'https://www.patreon.com/offen'
LINKEDIN_URL = 'https://www.linkedin.com/company/hioffen'
TWITTER_URL = 'https://twitter.com/hioffen'
RELEASE_DIRECT_URL = 'https://get.offen.dev'
HEROKU_DIRECT_URL = 'https://heroku.com/deploy?template=https://github.com/offen/heroku/tree/master'

OFFEN_ACCOUNT_ID = os.environ.get('OFFEN_ACCOUNT_ID', None)
