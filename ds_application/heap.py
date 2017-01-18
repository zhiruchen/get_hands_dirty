# encoding: utf-8

"""
二叉堆
"""


class Heap(object):
    """"""
    def __init__(self):
        self._heaplist = []
        self._currentsize = 0

    def insert(self, val):
        self._heaplist.append(val)
        self._currentsize += 1
        self.adjust(self._currentsize)

    def adjust(self, pos):
        """如果子节点的值比父节点的小，则交换二者的值"""
        while pos / 2 > 0:
            child_pos = pos
            parent_pos = pos / 2
            child_val = self._heaplist[child_pos]
            parent_val = self._heaplist[parent_pos]
            if child_val < parent_val:
                self._heaplist[child_pos], self._heaplist[parent_pos] = parent_val, child_val

            pos /= 2

    def del_min(self):
        min_val = self._heaplist[1]
        self._heaplist[1] = self._heaplist[self._currentsize]
        self._currentsize -= 1
        self.sift_down(1)

    def sift_down(self, pos):
        while (pos * 2) <= self._currentsize:
            min_pos = self.get_min_pos(pos)
            if self._heaplist[pos] > self._heaplist[min_pos]:
                self._heaplist[pos], self._heaplist[min_pos] = \
                    self._heaplist[min_pos], self._heaplist[pos]
            pos = min_pos

    def get_min_pos(self, pos):
        """返回两个子节点中较小的值的位置"""
        if (pos * 2 + 1) > self._currentsize:
            return pos * 2
        else:
            if self._heaplist[pos*2] < self._heaplist[pos*2+1]:
                return pos * 2
            else:
                return pos * 2 + 1

    def build_heap(self, keys):
        self._currentsize = len(keys)
        self._heaplist = [None] + keys[:]

        pos = self._currentsize / 2
        while pos > 0:
            self.sift_down(pos)
            pos -= 1
