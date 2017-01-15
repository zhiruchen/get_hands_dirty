# encoding: utf-8

"""
约瑟夫问题
http://interactivepython.org/runestone/static/pythonds/BasicDS/SimulationHotPotato.html
"""
from datastructure.queue import Queue


def hot_potato(name_list, num):
    queue = Queue()

    for name in name_list:
        queue.enqueue(name)

    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())

        queue.dequeue()

    return queue.dequeue()


def test_hot_potato():
    assert hot_potato("a b c d e".split(), 3) == 'a'
    assert hot_potato("1 2 3".split(), 1) == '3'
