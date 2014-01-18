import .feeds
from os.path import exists
if exists('~/.newsic/feeds.txt'):
    feeds = open('~/.newsic/feeds.txt').read()

bleah = [ Feed(url) for url in feeds.split('\n') ]

for b in bleah:
    b.display()
