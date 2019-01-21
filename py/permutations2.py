# Given a collection of numbers that might contain duplicates,
# return all possible unique permutations.
#
# Example:
#
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]


from typing import List


class Solution:
    def permute_unique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(begin, nums):
            if begin == end:
                permutations.append(nums)

            for i in range(begin, end):
                if i != begin and nums[i] == nums[begin]:
                    continue

                nums[begin], nums[i] = nums[i], nums[begin]
                backtrack(begin + 1, nums[:])

        nums.sort()
        permutations = []
        end = len(nums)
        backtrack(0, nums[:])

        return permutations
