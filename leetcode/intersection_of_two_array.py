class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        import bisect
        if len(nums1) <= len(nums2):
            short_list = nums1
            long_list = nums2
        else:
            short_list = nums2
            long_list = nums1


        intersection_list = []
        long_list.sort()
        for x in short_list:
            j = bisect.bisect_left(long_list, x)
            if j != len(long_list) and long_list[j] == x:
                intersection_list.append(x)

        return list(set(intersection_list))

if __name__ == '__main__':
    su = Solution()
    print(su.intersection([3,1,2], [1,1]))