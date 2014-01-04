import unittest
from news import Feed
from news import Config

class TestFeedFetchFromURL(unittest.TestCase):
    def SetUp():
        urls = ['http://news.ycombinator.com/rss']

    def test_fetch(urls):
        feeds = [ Feed(url) for url in urls ]
        self.assertTrue(len(feeds) > 0)

if __name__=='__main__':
    unittest.main()
