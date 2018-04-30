# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.


from typing import List


class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        strs_len = len(strs)
        if strs_len == 0:
            return ""

        prefix_len = 0
        min_len = min([len(s) for s in strs])

        for i in range(min_len):
            char = strs[0][i]
            for j in range(1, strs_len):
                if strs[j][i] != char:
                    return strs[0][0:prefix_len]

            prefix_len += 1

        return strs[0][0:prefix_len]
