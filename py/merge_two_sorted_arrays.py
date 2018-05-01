# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
#
# * The number of elements initialized in nums1 and nums2 are m and n respectively.
# * You may assume that nums1 has enough space (size that is greater or equal to m + n)
#   to hold additional elements from nums2.
#
# Example:
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]


from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        nums0 = nums1
        nums1 = nums0[:m]

        i = 0
        j = 0
        for k in range(m + n):
            if i == m:
                nums0[k:] = nums2[j:]
                break
            elif j == n:
                nums0[k:] = nums1[i:]
                break
            elif nums1[i] < nums2[j]:
                nums0[k] = nums1[i]
                i += 1
            else:
                nums0[k] = nums2[j]
                j += 1

        return nums0  # for test
