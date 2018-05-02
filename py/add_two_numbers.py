# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#
# Explanation: 342 + 465 = 807.


from py.collections.list import ListNode


class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        cur = result
        while l1.next and l2.next:
            x, cur.val = divmod(l1.val + l2.val + cur.val, 10)
            cur.next = ListNode(x)
            cur = cur.next
            l1, l2 = l1.next, l2.next

        x, cur.val = divmod(l1.val + l2.val + cur.val, 10)
        l1 = l2 if l2.next else l1

        while l1.next:
            l1 = l1.next
            cur.next = ListNode(x)
            cur = cur.next
            x, cur.val = divmod(l1.val + cur.val, 10)

        if x != 0:
            cur.next = ListNode(x)

        return result
