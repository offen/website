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
    # maps any CSS selector to a list of classes to be added
    # 'p': ['pv0', 'dim']
}

GITHUB_ORG = 'https://github.com/offen'
CONTACT_EMAIL = 'hioffen@posteo.de'
GPG_KEY_FILE = '74B041E23DB29D552644CEB1B18C633D6967FE3F.asc'
PATREON_URL = 'https://www.patreon.com/offen'
LINKEDIN_URL = 'https://www.linkedin.com/company/hioffen'
TWITTER_URL = 'https://twitter.com/hioffen'

OFFEN_ACCOUNT_ID = '9b63c4d8-65c0-438c-9d30-cc4b01173393'
