# encoding: utf-8

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = []
        for x in nums:
            count = 0
            if x == 1:
                count += 1
            else:
                if count:
                    ones.append(count)
                    count = 0

        ones.append(count)
        return max(ones)