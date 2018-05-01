# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
#
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


class Solution:
    def str_str(self, haystack: str, needle: str) -> int:
        m = len(needle)
        if m == 0:
            return 0

        i = 0
        j = 0
        idx = -1
        n = len(haystack)

        while i < n:
            if haystack[i] == needle[j]:
                j += 1
                if idx == -1:
                    idx = i

                if j == m:
                    return idx
            else:
                i -= j
                j = 0
                idx = -1

            i += 1

        return -1
