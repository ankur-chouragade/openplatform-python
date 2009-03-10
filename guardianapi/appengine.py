from google.appengine.api import memcache
from fetchers import HttpCacheFetcher

class AppEngineFetcher(HttpCacheFetcher):
    def __init__(self):
        super(AppEngineFetcher, self).__init__(memcache)
