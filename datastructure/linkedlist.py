# encoding: utf-8


class Node(object):
    """链表结点"""
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, val):
        self._data = val

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_p):
        self._next = next_p


class LinkedList(object):
    def __init__(self):
        self._head = None
        self._size = 0

    def add(self, data):
        temp = Node(data)
        temp.next = self._head
        self._head = temp
        self._size += 1

