# encoding: utf-8

import random

"""查找无序数组中的中位数"""

from quick_sort import partition


def find_mid_number(number_list):
    len_number = len(number_list)
    low, high = 0, len_number - 1
    mid_index = len_number / 2

    while high > low:
        j = partition(number_list, low, high)

        if j == mid_index:
            return number_list[j]
        elif j > mid_index:
            high = j - 1
        else:
            low = j + 1


def test_find_mid():
    alist = [random.randint(1, 100) for _ in range(10)]
    print alist
    soerted_a = sorted(alist)
    print soerted_a
    print soerted_a[len(alist)/2]
    print find_mid_number(alist)
