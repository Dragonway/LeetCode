# Given a sorted integer array without duplicates, return the summary of its ranges.
#
#
# Example 1:
#
# Input: [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
#
#
# Example 2:
#
# Input: [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]


from typing import List


class Solution:
    def summary_ranges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        summary = []

        n = len(nums)
        left = 0
        for i in range(1, n):
            if nums[i] - nums[i-1] != 1:
                summary.append(str(nums[left]) if left == i-1 else '%s->%s' % (nums[left], nums[i-1]))
                left = i

        summary.append(str(nums[left]) if left == n-1 else '%s->%s' % (nums[left], nums[n-1]))
        return summary
