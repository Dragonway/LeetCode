# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(begin):
            if begin == end:
                permutations.append(nums[:])

            for i in range(begin, end):
                nums[begin], nums[i] = nums[i], nums[begin]
                backtrack(begin + 1)
                nums[begin], nums[i] = nums[i], nums[begin]

        permutations = []
        end = len(nums)
        backtrack(0)

        return permutations
