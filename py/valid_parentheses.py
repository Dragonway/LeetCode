# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
#
# Note that an empty string is also considered valid.
#
#
# Example 1:
#
# Input: "()"
# Output: true
#
#
# Example 2:
#
# Input: "()[]{}"
# Output: true
#
#
# Example 3:
#
# Input: "(]"
# Output: false
#
#
# Example 4:
#
# Input: "([)]"
# Output: false
#
#
# Example 5:
#
# Input: "{[]}"
# Output: true


class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        brackets_map = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in brackets_map.values():
                stack.append(c)
            elif not stack or stack.pop() != brackets_map[c]:
                    return False

        return not stack
