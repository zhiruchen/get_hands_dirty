# coding: utf-8

"""数组相关"""


def find_showed_half_length_num(array):
    """数组中有一个数字出现的次数超过了数组长度的一半，找出这个数字"""
    times = 1
    current_num = array[0]

    for num in array[1:]:
        if num == current_num:
            times += 1
        else:
            times -= 1
            if times < 0:
                current_num = num
                times = 1

    return current_num
