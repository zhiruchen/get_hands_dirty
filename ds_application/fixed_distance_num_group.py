# encoding: utf-8

"""
在一个无序数组中找到数据之间的差值(绝对值)是一个定值的数字对数
"""


def find_group_number(array, distance):
    new_array = sorted(array)  # 先排序

    count = 0
    i, j = 0, 1
    while j < len(new_array):
        _dist = abs(new_array[i] - new_array[j])
        if _dist < distance:
            j += 1
        elif _dist > distance:
            i += 1
        else:
            count += 1
            i, j = i + 1, j + 1

    return count


def test_find_group_number():
    array = [1, 3, 4, 6, 9]
    print find_group_number(array, 3)

    array = [1, 22, 11, 2, 13, 6, 17, 0, 99, 88]
    print find_group_number(array, 11)
