# encoding: utf-8

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = "{0:b}".format(x)
        y = "{0:b}".format(y)

        print x, y
        
        if len(x) > len(y):
            y = ''.join(['0' for _ in range(len(x)- len(y))]) + y
        else:
            x = ''.join(['0' for _ in range(len(y)- len(x))]) + x
            
        count = 0
        for e1, e2 in zip(x, y):
            if e1 != e2:
                count += 1
        
        return count

if __name__ == '__main__':
    ss = Solution()
    print ss.hammingDistance(4, 1)