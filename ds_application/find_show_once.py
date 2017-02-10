# encoding: utf-8

"""
找到整数数组中只出现一次的数字，其他的数字都出现两次
"""


def find_once(mlist):
    """相同的数异或为0"""
    result = mlist[0]
    for x in mlist[1:]:
        result ^= x

    return result


def test_find_once():
    mlist = [1, 2, 3, 1, 2, 3, 6]
    print find_once(mlist)
