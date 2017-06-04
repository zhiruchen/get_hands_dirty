# encoding: utf-8

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = "{0:b}".format(num)
        rnum = 0
        l = len(nums)
        for i, x in enumerate(nums):
            rx = 1 if x == '0' else 0
            print rx
            rnum = rnum + rx * (2 ** ((l - 1) - i))
            
        return rnum

if __name__ == '__main__':
    su = Solution()
    print su.findComplement(5)