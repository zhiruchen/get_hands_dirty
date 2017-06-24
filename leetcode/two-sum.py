class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        import bisect
        high = bisect.bisect_left(numbers, target)
        half = target / 2
        _nums = numbers[:high]
        high1 = bisect.bisect_left(_nums, half)
        low1 = bisect.bisect_right(_nums, half)

        half_right_nums = _nums[low1:]

        for i, x in enumerate(_nums[:high1]):
            y = target - x
            j = bisect.bisect_left(half_right_nums, y)
            if j != len(_nums[low1:]) and half_right_nums[j] == y:
                return i+1, j + high1 +1


if __name__ == '__main__':
    su = Solution()
    print(su.twoSum([2,7,11,15], 9))

    print(su.twoSum([1,3,4,5,6,10], 7))