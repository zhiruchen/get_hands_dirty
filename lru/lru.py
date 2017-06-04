# encoding: utf-8

"""
LRU Algorithm demo
http://www.geeksforgeeks.org/implement-lru-cache/
https://github.com/golang/groupcache/blob/master/lru/lru.go
https://www.cs.jhu.edu/~yairamir/cs418/os6/sld020.htm
"""

MAXCACHESIZE = 4

class Cache(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.ll = []
        self.cache = {}

    def move_to_front(self, e):
        if self.ll.index(e) == 0:
            return
        self.ll.remove(e)
        self.ll = [e] + self.ll

    def remove_oldest(self):
        key = self.ll[-1]
        self.ll.remove(key)
        del self.cache[key]


    def add(self, key, val):
        v = self.cache.get(key)
        if v is not None:  # 缓存命中
            self.move_to_front(key)
            self.cache[key] = val
            return

        self.ll.insert(0, key)
        self.cache[key] = val

        if self.maxsize and len(self.ll) > self.maxsize:
            self.remove_oldest()

    def get(self, key):
        if not self.ll:
            return None, False
        v = self.cache.get(key)
        if v is not None:
            self.move_to_front(key)
            return v, True

        return None, False
