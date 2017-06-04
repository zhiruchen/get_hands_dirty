# encoding: utf-8

class TreeNode(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def t2s(t, ll):
            if t is None:
                return
            ll.append(str(t.val))
            if (not t.left) and t.right:
                ll.append('()')

            if t.left:
                ll.append('(')
                t2s(t.left, ll)
                ll.append(')')

            if t.right:
                ll.append('(')
                t2s(t.right, ll)
                ll.append(')')
        ll = []
        t2s(t, ll)
        return ''.join(ll)


if __name__ == '__main__':
    t = TreeNode(1, TreeNode(2, TreeNode(4, None, None), None), TreeNode(3, None, None))
    s = Solution()
    print s.tree2str(t)

    t = TreeNode(1, TreeNode(2, None, TreeNode(4, None, None)), TreeNode(3, None, None))
    print s.tree2str(t)
    