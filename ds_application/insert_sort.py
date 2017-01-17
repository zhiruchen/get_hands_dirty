# encoding: utf-8

"""
插入排序
"""


def insert_sort(mlist):
    llen = len(mlist)
    for i in range(1, llen):
        pos = i
        value = mlist[i]
        while pos > 0 and mlist[pos-1] > value:
            mlist[pos] = mlist[pos-1]
            pos -= 1

        mlist[pos] = value

    return mlist
