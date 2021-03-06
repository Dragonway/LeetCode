# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


from typing import Optional
from py.collections.list import ListNode


class Solution:
    def merge_two_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2

        if not l2:
            return l1

        if l1.val < l2.val:
            l0 = l1
            l1 = l1.next
        else:
            l0 = l2
            l2 = l2.next

        cur = l0
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 or l2
        return l0
