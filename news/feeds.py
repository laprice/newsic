
class Feed():
    """
    Feed objects are the primary abstraction used.
    
    At minimum they have a source_url and an empty History
    
    There can be multiple flavors (for instance Twitter feeds are fetched as json).
    """
    def __init__(self, source, **kwargs):
        self.source = source
        if history:
            self.history = History(history)
        if title:
            self.title
        else:
            self.title = self.source

    def __str__(self):
        template = """title: %(title)s\nsource: %(source)s"""
        

class History():
    def __init__(self, history_label):
        self.label = history_label # primary key for history objects
        

    

    
