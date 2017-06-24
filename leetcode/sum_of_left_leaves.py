# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sum_left(root, is_left):
            if root == None:
                return 0
            if root.left == None and root.right == None:
                if is_left:
                    return root.val
                else:
                    return 0
            else:
                return sum_left(root.left, True) + sum_left(root.right, False)

        if root == None:
            return 0

        return sum_left(root.left, True) + sum_left(root.right, False)
