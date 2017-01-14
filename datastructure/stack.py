# -*- encoding: utf-8 -*-

"""
https://zh.wikipedia.org/wiki/%E5%A0%86%E6%A0%88
https://docs.python.org/2/tutorial/datastructures.html
"""


class Stack(object):
    """栈是一种LIFO的线性数据结构"""
    def __init__(self):
        self._array = []

    def __len__(self):
        return len(self._array)

    def is_empty(self):
        return False if self._array else True

    def push(self, val):
        """入栈"""
        self._array.append(val)

    def pop(self):
        """弹栈 弹出最近入栈的值"""
        if self.is_empty():
            return None

        return self._array.pop()

    def peek(self):
        """返回栈顶值，但不删除"""
        if self.is_empty():
            return None

        return self._array[-1]
