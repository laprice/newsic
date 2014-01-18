import feeds
import os.path as op
import pprint

if op.exists('~/.newsic/feeds.txt'):
    print "found feeds.txt"
    myfeeds = open('~/.newsic/feeds.txt').read().split('\n')
else:
    print "gah!!! no feeds.txt giving you stupid"
    myfeeds = ['https://news.ycombinator.com/rss']

bleah = [ feeds.Feed(url) for url in myfeeds ]
counts = [ (f.title, f.fetch() ) for f in bleah ]


for b in bleah:
    b.display()
