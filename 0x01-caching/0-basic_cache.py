#!/usr/bin/env python3
"""
Create a class BasicCache that inherits
from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
This caching system doesn’t have limit
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ inheriting from BaseCaching which already exist"""
    def __init__(self):
        """ summary """
        super().__init__()

    def put(self, key, item):
        """
        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is not None or item is not None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Args:
            key (_type_): _description_
        """
        if key is not None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
