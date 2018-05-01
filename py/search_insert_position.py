# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
#
# Example 1:
#
# Input: [1,3,5,6], 5
# Output: 2
#
#
# Example 2:
#
# Input: [1,3,5,6], 2
# Output: 1
#
#
# Example 3:
#
# Input: [1,3,5,6], 7
# Output: 4
#
#
# Example 4:
#
# Input: [1,3,5,6], 0
# Output: 0


from typing import List


class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        if not nums or nums[0] > target:
            return 0

        n = len(nums)
        if nums[n-1] < target:
            return n

        left = 0
        right = n
        while left != right:
            mid = left + (right - left) // 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1

        return right
