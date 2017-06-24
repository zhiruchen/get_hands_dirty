# encoding: utf-8
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums):
            pos = i
            if nums[i] == 0:
                while pos < (len(nums)-1):
                    if nums[pos+1] == 0:
                        pos = pos + 1
                    else:
                        pos = pos + 1
                        break

                if pos != i:
                    nums[i], nums[pos] = nums[pos], nums[i]
                i = i + 1
            else:
                i = i + 1
        return nums

if __name__ == '__main__':
    su = Solution()
    nums = [0, 1, 0, 3, 12]
    nums = su.moveZeroes(nums)
    print(nums)

    nums = [0]
    nums = su.moveZeroes(nums)
    print(nums)

    nums = [1,2,3]
    nums = su.moveZeroes(nums)
    print(nums)

    nums = [1,0,2,0,3,4,5,0]
    nums = su.moveZeroes(nums)
    print(nums)
