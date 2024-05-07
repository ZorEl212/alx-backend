#!/usr/bin/env python3
""""FIFO Cacheing system"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """"Class to implement Fifo cacheing"""

    def __int__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        if key is None or item is None:
            return
        if len(self.cache_data) >= super().MAX_ITEMS:
            if key not in self.cache_data.keys():
                k = list(self.cache_data.keys())[0]
                self.cache_data.pop(k)
                print(f"DISCARD: {k}")
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
