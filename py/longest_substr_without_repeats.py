# Given a string, find the length of the longest substring without repeating characters.
#
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3.
#
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def length_of_longest_substr(self, s: str) -> int:
        pos = 0
        long = 0
        map_appearances = [False] * 256

        for i, c in enumerate(s):
            if map_appearances[ord(c)]:
                long = max(long, i - pos)
                while c != s[pos]:
                    map_appearances[ord(s[pos])] = False
                    pos += 1
                pos += 1
            else:
                map_appearances[ord(c)] = True

        long = max(long, len(s) - pos)
        return long
