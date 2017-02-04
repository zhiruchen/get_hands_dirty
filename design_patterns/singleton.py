# encoding: utf-8

"""
Python Impl of Singleton Design Pattern
"""

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        print "calling Singleton"
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class MyClass(object):
    __metaclass__ = Singleton


def test_singleton():
    assert id(MyClass()) == id(MyClass())
    print id(MyClass()) == id(MyClass())  # True
