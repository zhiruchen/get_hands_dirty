# encoding: utf-8

"""
 碾平多级列表
 有一个列表，当中有数字也有列表，列表中又有列表(多级列表)，现将之碾平
"""

queue = []


def flatten_list(data_list):
    if isinstance(data_list, int):
        queue.append(data_list)
    else:
        if data_list:
            for item in data_list:
                flatten_list(item)
        else:
            return


def test_flattern_list():
    mlist = [1, 2, [3, 4], [5, [6, [7, [8, 9]]]], [100]]
    flatten_list(mlist)
    print queue
