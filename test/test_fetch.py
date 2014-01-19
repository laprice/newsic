from os.path import abspath, dirname
import sys
import unittest
sys.path.append(dirname(dirname(abspath(__file__))))
from news import *


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

    def test_feed_parse(self):
        n = self.f[0]
        n.fetch()
        self.assertIsInstance(n.current_items,type([]))

    def test_display(self):
        for f in self.feedlist:
            self.AssertEquals(len(f.current_items),len(self.display().split('\n')))

if __name__=='__main__':
    unittest.main()
