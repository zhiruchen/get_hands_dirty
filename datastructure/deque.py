# -*-encoding：utf-8 -*-


class Deque(object):
    """双端队列"""
    def __init__(self):
        self._item = []

    def add_front(self, item):
        """添加item到front"""
        self._item.append(item)

    def add_rear(self, item):
        """添加item到rear"""
        self._item.insert(0, item)

    def remove_front(self):
        """removes the front item from the deque"""
        return self._item.pop()

    def remove_rear(self):
        """removes the rear item from the deque"""
        return self._item.pop(0)

    def is_empty(self):
        return self._item == []

    def size(self):
        return len(self._item)
