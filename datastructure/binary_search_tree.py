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
    def __init__(self, arg):
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
