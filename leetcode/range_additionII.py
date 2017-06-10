# encoding: utf-8

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        matrix = []
        for _ in range(m):
            ll = []
            for _ in range(n):
                ll.append(0)
            matrix.append(ll)

        maxd = 0
        for x in ops:
            a, b = x
            for i in range(a):
                for j in range(b):
                    matrix[i][j] += 1
                    maxd = matrix[i][j] if matrix[i][j] > maxd else maxd

        count = 0
        for x in matrix:
            count += x.count(maxd)

        return count

if __name__ == '__main__':
    su = Solution()
    print su.maxCount(3,3,[[2,2],[3,3]])