# -*-encoding: utf-8 -*-


class Queue(object):
    """队列(先进先出)"""
    def __init__(self):
        self._item = []

    def is_empty(self):
        return self._item == []

    def enqueue(self, val):
        self._item.insert(0, val)

    def dequeue(self):
        return self._item.pop()

    def size(self):
        return len(self._item)
