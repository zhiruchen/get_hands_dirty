# coding: utf-8

"""
二叉树
"""


class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

    @property
    def data(self):
        return self._data

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, new_left):
        self._left = new_left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, new_right):
        self._right = new_right


class BinTree(object):
    def __init__(self, root):
        self._root = root

    def pre_order(self):
        """前序便利"""
        self._pre_order(self._root)

    def _pre_order(self, root):
        if root:
            print root.data
            self._pre_order(root.left)
            self._pre_order(root.right)

    def mid_order(self):
        def _mid_order(root):
            if root:
                _mid_order(root.left)
                print root.data
                _mid_order(root.right)

        _mid_order(self._root)

    def post_order(self):
        """后序遍历"""
        def _post_order(root):
            if root:
                _post_order(root.left)
                _post_order(root.right)
                print root.data

        _post_order(self._root)

    def level_order(self):
        """层次序便利"""
        queue = [self._root]

        while queue:
            node = queue.pop(0)
            print node.data
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def mirror_tree(self):
        """二叉树镜像"""
        def _mirror_tree(root):
            if root:
                if root.left or root.right:
                    root.left, root.right = root.right, root.left
                    _mirror_tree(root.left)
                    _mirror_tree(root.right)

        _mirror_tree(self._root)


def is_subtree(t1_root, t2_root):
    if not t2_root:
        return True

    if not t1_root:
        return False

    if t1_root.data != t2_root.data:
        return False

    return is_subtree(t1_root.left, t2_root.left) and is_subtree(t1_root.right, t2_root.right)


def has_subtree(root1, root2):
    result = False
    if root1 and root2:
        if root1.data == root2.data:
            result = is_subtree(root1, root2)

        if not result:
            result = has_subtree(root1.left, root2)

        if not result:
            result = has_subtree(root1.right, root2)

    return result


def test_bin_tree():
    bin_tree = BinTree(TreeNode(1,
                                left=TreeNode(2, left=TreeNode(3), right=None),
                                right=TreeNode(4, left=TreeNode(5), right=TreeNode(6))))
    # bin_tree.pre_order()  # 1 2 3 4 5 6
    # print "+" * 10
    # bin_tree.mid_order()  # 3 2 1 5 4 6
    # print "+" * 10
    # bin_tree.post_order()  # 3 2 5 6 4 1
    # print "+" * 10
    # bin_tree.level_order()  # 1 2 4 3 5 6
    bin_tree.mirror_tree()
    bin_tree.pre_order()  # 1 4 6 5 2 3


def test_has_subtree():
    tree1 = BinTree(TreeNode(1,
                                left=TreeNode(2, left=TreeNode(3), right=None),
                                right=TreeNode(4, left=TreeNode(5), right=TreeNode(6))))
    tree2 = BinTree(TreeNode(4, left=TreeNode(5), right=TreeNode(6)))

    print tree1._root.data, tree2._root.data
    print has_subtree(tree1._root, tree2._root)  # True
