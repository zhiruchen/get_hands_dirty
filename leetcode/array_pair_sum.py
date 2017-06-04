# encoding: utf-8
"""https://leetcode.com/problems/array-partition-i/#/description"""

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum = 0
        i = 0
        while i < len(nums) - 1:
            sum = sum + nums[i]
            i = i + 2
            
        return sum