# encoding: utf-8

"""
递归求列表元素之和
"""

def sum_of_list(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + sum_of_list(num_list[1:])
