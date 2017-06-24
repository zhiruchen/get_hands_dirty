# encoding: utf-8 

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        import functools
        def getdg(num):
            if num <= 10:
                return [num]
            nums = []
            while num > 0:
                nums.append(num % 10)
                num = num // 10
            return nums

        def add(x, y):
            return x + y
        
        if num <= 10:
            if num < 10:
                return num
            return 1
        
        while num > 10:
            nsum = functools.reduce(add, getdg(num), 0)
            if nsum <= 10:
                if nsum < 10:
                    return nsum
                return 1
            
            num = nsum

        
        