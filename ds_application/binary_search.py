# encoding: utf-8

"""
二分查找, 前提是序列有序
"""


def bin_search(item_list, val):
    low = 0
    high = len(item_list) - 1
    found = False

    while low <= high and not found:
        mid = (low + high) / 2
        if val == item_list[mid]:
            found = True
        elif val < item_list[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return found


def test_bin_search():
    assert bin_search([1,2,3,4,5], 3) is True
    assert bin_search([1,6,9,10], 0) is False


def recur_bin_search(item_list, val):
    """递归版二分查找"""
    if not item_list:
        return False
    else:
        mid = len(item_list) / 2
        if item_list[mid] == val:
            return True
        else:
            if val < item_list[mid]:
                return recur_bin_search(item_list[:mid], val)
            else:
                return recur_bin_search(item_list[mid+1:], val)


def test_recur_bin_search():
    assert recur_bin_search([1,2,3,4,5], 3) is True
    assert recur_bin_search([1,6,9,10], 0) is False
