# encoding: utf-8


class Map(object):
    def __init__(self):
        self._size = 11
        self._slots = [None] * seld._size

    def hash_func(self, key):
        return key % self._size

    def put(self, key, val):
        pass

    def get(self, default=None):
        pass

    
