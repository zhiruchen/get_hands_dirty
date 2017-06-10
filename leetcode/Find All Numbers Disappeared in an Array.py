# encoding: utf-8

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ll = []
        ns = set(nums)
        for i in range(1, len(nums)+1):
            if i not in ns:
                ll.append(i)

        return ll
