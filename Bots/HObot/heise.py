from __future__ import with_statement
import feedparser

import contextlib
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

def feed_head(feed='https://www.heise.de/rss/heise-atom.xml'):
    d = feedparser.parse(feed)
    headlines = []
    for i in range(10):
        lnk = shorten_url(d.entries[i].link)
        headlines.append(d.entries[i].title+": "+lnk)
    return "\n".join(headlines)


def shorten_url(url):
    request_url = ('http://tinyurl.com/api-create.php?' +
    urlencode({'url':url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')
