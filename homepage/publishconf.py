# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = os.environ.get('SITEURL', 'https://www.offen.dev')
# RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

DELETE_OUTPUT_DIRECTORY = True

PLUGINS += ['optimize_images']
