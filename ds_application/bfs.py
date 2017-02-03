# encoding: utf-8

"""
广度优先遍历
"""
from datastructure.queue import Queue
from datastructure.graph import build_graph


def bfs(root):

    s = set()
    q = Queue()

    q.enqueue(root)
    while not q.is_empty():
        current = q.dequeue()
        print current.id
        for v in current.get_connections():
            if v not in s:
                s.add(v)
                q.enqueue(v)


def test_bfs():
    root = build_graph()
    bfs(root)  # 0 1 5 2 4 3 0
