import unittest
import sys
sys.path.append('..')
from feeds import Feed


class TestFeedFetchFromURL(unittest.TestCase):
    def setUp(self):
        self.feedlist = [ 'http://news.ycombinator.com/rss' ]
    
    def test_feeds(self):
        f = [ Feed(feed) for feed in self.feedlist ]
        n = f.pop()
        self.assertIsInstance(Feed,n)

if __name__=='__main__':
    unittest.main()
