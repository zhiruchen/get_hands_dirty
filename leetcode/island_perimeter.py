# encoding: utf-8
"""https://leetcode.com/problems/island-perimeter/#/description"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def around(grid, i, j):
            count = 0
            if i == 0:
                if j == 0 or (j == (len(grid[i])-1)):
                    count += 2
                    if j == 0 and len(grid[i]) == 1:
                        if grid[i+1]
                else:
            elif i == (len(grid)-1):
                if j == 0 or (j == (len(grid[i])-1)):
                    count += 2
                else:




        perimeter = 0
        if len(grid) == 1:
            count = 0
            for i, x in enumerate(grid):
                for j, y in enumerate(x):
                    if y == 1:
                        if j == 0:
                            count += 3
                            if j+1 < len(x):
                                if x[j+1] != 1:
                                    return count
                            else:
                                return count
                        elif j == len(x) -1:
                            

        for i, x in enumerate(grid):
            for j, y in enumerate(x):
                count = 0
                if y == 1:
                    if i == 0:
                        if j == 0:
