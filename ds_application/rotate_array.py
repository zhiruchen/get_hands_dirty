# encoding: utf-8

"""
旋转数组
"""


def reverse(array, start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1


def rotate_array(array, n):
    """
    :param array:
    :param n: 旋转左边的前n个元素
    :return:
    """
    reverse(array, 0, n-1)
    reverse(array, n, len(array)-1)
    reverse(array, 0, len(array)-1)


def test_rotate():
    mlist = [1, 2, 3, 4, 5]
    rotate_array(mlist, 2)  # [3, 4, 5, 1, 2]
    print mlist
