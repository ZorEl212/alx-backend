#!/usr/bin/env python3
"""Basic Caching algorithm"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic caching system"""
    def put(self, key, item):
      """Add an item """
      if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
