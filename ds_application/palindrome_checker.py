# encoding: utf-8

"""
回文字符串检查
"""
from datastructure.deque import Deque


def palindrome_checker(str):
    deque = Deque()
    for s in str:
        deque.add_rear(s)

    while deque.size() > 1:
        if deque.remove_front() == deque.remove_rear():
            continue
        else:
            return False

    return deque.size() == 0 or deque.size() == 1


def test_palindrome_checker():
    assert palindrome_checker("aba") is True
    assert palindrome_checker("121") is True
    assert palindrome_c  hecker("roor") is True
    assert palindrome_checker("lsdkjfskf") is False
