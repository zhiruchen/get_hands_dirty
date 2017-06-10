# encoding: utf-8

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        x = '{0:b}'.format(a)
        y = '{0:b}'.format(b)

        