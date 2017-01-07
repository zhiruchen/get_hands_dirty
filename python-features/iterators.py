# -*- encoding: utf-8 -*-

"""
迭代器
http://anandology.com/python-practice-book/iterators.html
http://nvie.com/posts/iterators-vs-generators/
迭代器一定是可迭代的，
"""

from collections import Iterable, Iterator


class yrange(object):
    """迭代器，yrange的对象既是可迭代的也是迭代器"""
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


class zrange(object):
    """zrange的实例仅是可迭代的"""
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return zrange_iter(self.n)


class zrange_iter(object):
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


class reverse_iter(object):
    """反向迭代器"""
    def __init__(self, lst):
        self.lst = lst
        self.start = -1
        self.end = 0 - len(lst)

    def __iter__(self):
        return self

    def next(self):
        if self.start >= self.end:
            index = self.start
            self.start -= 1
            return self.lst[index]
        raise StopIteration()


def test_yrange():
    assert list(yrange(4)) == [0, 1, 2, 3]
    assert sum(yrange(4)) == 6
    assert isinstance(yrange(3), Iterable) is True
    assert isinstance(yrange(3), Iterator) is True


def test_zrange():
    z = zrange(4)
    z_list1 = list(z)
    z_list2 = list(z)
    assert z_list1 == [0, 1, 2, 3]
    assert z_list2 == [0, 1, 2, 3]
    assert isinstance(z, Iterable) is True
    assert isinstance(z, Iterator) is False

if __name__ == '__main__':
    test_yrange()
    test_zrange()
