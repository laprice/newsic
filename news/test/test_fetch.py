import unittest
import sys
sys.path.append('..')
from feeds import Feed


class TestFeedFetchFromURL(unittest.TestCase):
    def setUp(self):
        self.feedlist = [ 'http://news.ycombinator.com/rss' ]
        self.f = [ Feed(feed) for feed in self.feedlist ]

    def test_feeds(self):
        n = self.f[0]
        self.assertIsInstance(n,Feed)

    def test_feed_repr(self):
        n = self.f[0]
        t = """title: http://news.ycombinator.com/rss
source: http://news.ycombinator.com/rss"""
        self.assertEquals(n.__str__(),t)

if __name__=='__main__':
    unittest.main()
