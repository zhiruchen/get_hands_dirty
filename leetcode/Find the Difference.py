# encoding: utf-8

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for x in t:
            if x not in s:
                return x