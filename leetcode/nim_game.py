# encoding: utf-8
"""https://leetcode.com/problems/nim-game/#/description"""

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        winner = "A"
        left = n
        
        while left:
            