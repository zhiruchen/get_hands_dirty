# encoding: utf-8

"""
深度优先遍历
"""
from datastructure.stack import Stack
from datastructure.graph import build_graph


def dfs(root):
    visited = {}
    dfs_helper(root, visited)


def dfs_helper(v, visited):
    visited[v.id] = True
    print v

    for nbr in v.get_connections():
        if visited.get(nbr.id, False) is False:
            dfs_helper(nbr, visited)


def dfs_unrecur(root):
    s = Stack()
    s.push(root)
    visited = {}

    while not s.is_empty():
        v = s.pop()
        if visited.get(v.id, False) is False:
            visited[v.id] = True
            print v

            for nbr in v.get_connections():
                s.push(nbr)


def test_dfs():
    root = build_graph()
    dfs(root)  # 0 1 2 3 4 5

    dfs_unrecur(root)  # 0 5 2 3 4 1
