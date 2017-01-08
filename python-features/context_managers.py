# -*- encoding: utf-8 -*-

"""
context manager
"""

from contextlib import contextmanager


class SimpleFileCloser(object):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        """打开并返回文件"""
        print "opening file"
        self._file = open(self.name, self.mode)
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """当离开with代码块的时候关闭文件描述符"""
        print "closing file"
        self._file.close()


def test_file():
    with SimpleFileCloser("myfile.txt", 'w') as f:
        f.write("test txt!")


# ---------------open file----------------
@contextmanager
def open_file(name, mode):
    _file = open(name, mode)
    yield _file
    _file.close()


def test_open_file():
    with open_file('my_file.txt', 'w') as f:
        f.write("context manager！")


if __name__ == '__main__':
    # test_file()
    test_open_file()
