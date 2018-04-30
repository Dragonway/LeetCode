# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        num_to_i = {}

        for i, num in enumerate(nums):
            search = target - num
            j = num_to_i.get(search, None)
            if j is not None:
                return [j, i]

            num_to_i[num] = i
