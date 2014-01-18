import feedparser
from hashlib import sha1

class Feed():
    """
    Feed objects are the primary abstraction used.
    
    At minimum they have a source_url and an empty History
    
    There can be multiple flavors (for instance Twitter feeds are fetched as json).
    """
    def __init__(self, source, **kwargs):
        self.source = source
        if kwargs.has_key('title'):
            self.title
        else:
            self.title = self.source
        if kwargs.has_key('history'):
            self.history = History(history)
        else:
            self.history = History(self.source)

    def __str__(self):
        template = """title: %(title)s\nsource: %(source)s"""
        return template % self.__dict__

    def fetch(self):
        self.raw = feedparser.parse(self.source)
        self.current_items = self.raw['items']
        self.history.update(self.raw)
        return len(self.current_items)

    def display(self):
        for i in self.current_items:
            print i['title'], ": ", i['link']


class History():
    def __init__(self, history_label):
        self.label = history_label # primary key for history objects
        
        self.recover(sha1(self.label))

    def recover(self, key):
        pass
    
    def update(self, raw):
        pass


    

    
