# encoding: utf-8

"""
二叉查找树
所有的左子树都小于父节点，所有的右子树都大于父节点.
"""


class TreeNode(object):
    """docstring for TreeNode."""
    def __init__(self, key, val, parent=None, left_child=None, right_child=None):
        self.key = key
        self.val = val
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

    def has_left_child(self):
        return self.left_child is not None

    def has_right_child(self):
        return self.right_child is not None


class BinarySearch(object):
    def __init__(self):
        self._root = None
        self._size = 0

    def size(self):
        return self._size

    def __iter__(self):
        return self._root.__iter__()

    def put(self, key, val):
        if self._root:
            self._put(key, val, self._root)
        else:
            self._root = TreeNode(key, val)
        self._size += 1

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)

    def __setitem__(self, k ,v):
        self.put(k ,v)

    def get(self, key):
        if self._root:
            res = self._get(key, self._root)
            if res:
                return res.val
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None

        if key == current_node.key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return self._get(key, self._root) is not None


def test_bin_search():
    bin_search = BinarySearch()
    bin_search.put(1, 1)
    bin_search.put(2, 2)
    bin_search.put(3, 3)
    bin_search.put(4, 4)

    assert bin_search.get(1) == 1
    assert bin_search.get(2) == 2
    assert bin_search[3] == 3
    assert bin_search[4] == 4
    for n in range(1, 5):
        if n in bin_search:
            print "%s is in bin_search" % n
