# encoding: utf-8
"""https://leetcode.com/problems/single-number/#/description
数字列表只有一个数出现了一次，其他的都出现了2次，找到出现一次的那个数
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums, 0)

