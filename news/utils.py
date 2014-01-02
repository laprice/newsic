import json
from .feeds import Feed

"""
This file contains non-core functionality.

Importing feeds from opml and google reader json blobs.
"""

def import_google_reader(blobfile):
    """hand it the path to a blobfile and get a list of Feed objects"""
    with open('feeds/feeds.json') as fd:
        feeds = json.load(fd)
    # magic happens here
    feeds = [ Feed(f) for f in feeds ]
    
