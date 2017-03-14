"""
AutoCanary | https://firstlook.org/code/autocanary
Copyright (c) 2015 First Look Media

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import feedparser

from . import common

config = {
    'feed_url': b'https://en.wikinews.org/w/index.php?title=Special:NewsFeed&feed=rss&categories=Published&notcategories=No%20publish|Archived|AutoArchived|disputed&namespace=0&count=5&ordermethod=categoryadd&stablepages=only',
    # --- waiting for unicode fix.
    #'headline_bullet': u"\u2022"
    'headline_bullet': '> '
}

class Headlines(object):
    def __init__(self):
        self.enabled = False
        self.have_headlines = False
        self.headlines_str = None

    def fetch_headlines(self):
        # --- feed.entries is empty list on fail.
        feed = feedparser.parse(config['feed_url'])

        # --- available keys: summary_detail published_parsed links title
        # comments summary guidislink title_detail link published id
        entry_data = list(map(lambda x: (x.title,), feed.entries))
        headlines = list(map(lambda x: "{}{}".format(config['headline_bullet'], x[0]), entry_data))
        if len(headlines) == 0:
            self.have_headlines = False
            common.alert("Couldn't fetch headlines.")
        else:
            self.have_headlines = True
            self.store_headlines(headlines)

    def store_headlines(self, headlines):
        self.headlines_str = '\n'.join(headlines)
