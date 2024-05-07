#!/usr/bin/env pyhon3
""""Basic Caching algorithm"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
