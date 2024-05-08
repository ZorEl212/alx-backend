#!/usr/bin/env python3
""""LIFO Cacheing System"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """"Class implementing LIFO Cache"""

    def __init__(self):
      """init method overriding super's"""
      super().__init__()
      self.cache_data = OrderedDict()

    def put(self, key, item):
      """Put a cache in lifo system"""
      if item is None or key is None:
          return None
      if len(self.cache_data) >= super().MAX_ITEMS:
          if key not in self.cache_data.keys():
                k = list(self.cache_data.keys())[-1]
                self.cache_data.popitem()
                print(f'DISCARD: {k}')
      self.cache_data[key] = item
      
      self.cache_data.move_to_end(key)

    def get(self, key):
      """Get a item by key if exists"""
      if key is None or key not in self.cache_data.keys():
          return None
      return self.cache_data[key]
