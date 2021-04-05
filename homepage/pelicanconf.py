import os
from datetime import datetime
from pelican_decorate_content import decorate_content

# If your site is available via HTTPS, make sure SITEURL begins with https://
RELATIVE_URLS = False

AUTHOR = 'offen'
SITENAME = 'Fair Web Analytics | Offen'
PATH = 'content'
TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'en'

BUILD_DATE = datetime.now()

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
DELETE_OUTPUT_DIRECTORY = False
CACHE_CONTENT = True

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
PLUGINS = [decorate_content, 'assets']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.fenced_code': {},
        'markdown_link_attr_modifier': {
            'auto_title': 'on',
            'new_tab': 'external_only',
        },
    },
    'output_format': 'html5',
}

DECORATE_CONTENT = {
    '[data-button]': ['w-100', 'w-auto-ns', 'tc', 'tl-ns', 'dib', 'mt3', 'ph4', 'pv2', 'b--solid', 'bw2'],
    '[data-button-mb5]': ['w-100', 'w-auto-ns', 'tc', 'tl-ns', 'dib', 'mt3', 'mb5', 'ph4', 'pv2', 'b--solid', 'bw2'],
    '[data-button-mb3]': ['w-100', 'w-auto-ns', 'tc', 'tl-ns', 'dib', 'mt3', 'mb3', 'ph4', 'pv2', 'b--solid', 'bw2'],
    '[data-button="outline"]': ['b--gray', 'gray'],
    '[data-button="full"]': ['cclr-brd-black-mid', 'white', 'cclr-bg-black-mid'],
    '[data-button-mb5="full"]': ['cclr-brd-black-mid', 'white', 'cclr-bg-black-mid'],
    'figure a': ['link'],
    'p a': ['link', 'b', 'dim'],
    'h1 a': ['link', 'b', 'dim'],
    'h2 a': ['link', 'b', 'dim'],
    'h3 a': ['link', 'b', 'dim'],
    'h4 a': ['link', 'b', 'dim'],
    'h5 a': ['normal', 'moon-gray'],
    'li a': ['link', 'b', 'dim'],
    'a:not([data-button])': ['gray'],
    'h1': ['f2', 'normal', 'lh-title', 'mt3', 'ma0', 'mb3'],
    'h2': ['f2', 'normal', 'lh-title', 'mt4', 'ma0', 'mb3'],
    'h3': ['f3', 'normal', 'mt5', 'ma0', 'mb3'],
    'h4': ['f5', 'normal', 'mt4', 'ma0', 'mb3'],
    'h5': ['f5', 'normal', 'mt5', 'ma0', 'mb1'], # text over button
    'h6': ['f5', 'lh-solid', 'normal', 'ma0', 'light-silver'], # not used
    'p': ['ma0', 'pb3'],
    'blockquote': ['f4', 'ma0', 'ph4-ns', 'pv3'],
    'blockquote p': ['nb2'],
    'hr': ['mt5', 'mb3', 'b--black-05']
}

GITHUB_REPO = 'https://github.com/offen/offen'
ROADMAP = 'https://github.com/offen/offen/projects/1'
CONTACT_EMAIL = 'hioffen@posteo.de'
PGP_KEY_FILE = '74B041E23DB29D552644CEB1B18C633D6967FE3F.asc'
PATREON_URL = 'https://www.patreon.com/offen'
LINKEDIN_URL = 'https://www.linkedin.com/company/hioffen'
TWITTER_URL = 'https://twitter.com/hioffen'
MASTODON_URL = 'https://fosstodon.org/@offen'
RELEASE_DIRECT_URL = 'https://get.offen.dev'
DOCKER_DIRECT_URL = 'https://hub.docker.com/r/offen/offen'
HEROKU_DIRECT_URL = 'https://heroku.com/deploy?template=https://github.com/offen/heroku/tree/master'
UBERSPACE_DIRECT_URL = 'https://lab.uberspace.de/guide_offen.html'
YUNOHOST_DIRECT_URL = 'https://github.com/offen/offen_ynh'
OFFEN_AUDITORIUM_URL = 'https://offen.offen.dev/auditorium/'
DOCS_URL = 'https://docs.offen.dev/'
DOCS_GETSTARTED_URL = 'https://docs.offen.dev/running-offen/'
DOCS_GETSTARTED_URL_CAMPAIGN = 'https://docs.offen.dev/running-offen/?utm_campaign=get-started'
DOCS_TRYDEMO_URL = 'https://docs.offen.dev/running-offen/test-drive/'
DOCS_TRYDEMO_URL_CAMPAIGN = 'https://docs.offen.dev/running-offen/test-drive/?utm_campaign=try-demo'

OFFEN_ACCOUNT_ID = os.environ.get('OFFEN_ACCOUNT_ID', None)
