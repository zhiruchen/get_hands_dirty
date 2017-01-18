# encoding: utf-8


def quick_sort(alist):
    do_sort(alist, 0, len(alist)-1)


def do_sort(alist, first, last):
    if first < last:
        _pos = partition(alist, first, last)
        do_sort(alist, first, _pos-1)
        do_sort(alist, _pos+1, last)


def partition(alist, first, last):
    pivot_value = alist[first]
    left_pos = first + 1
    right_pos = last

    done = False
    while not done:
        while left_pos <= right_pos and alist[left_pos] <= pivot_value:
            left_pos += 1

        while right_pos >= left_pos and alist[right_pos] >= pivot_value:
            right_pos -= 1

        if right_pos < left_pos:
            done = True
        else:
            alist[left_pos], alist[right_pos] = alist[right_pos], alist[left_pos]

    alist[first], alist[right_pos] = alist[right_pos], alist[first]
    return right_pos
