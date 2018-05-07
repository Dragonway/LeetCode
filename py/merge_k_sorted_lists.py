# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
#
# Output: 1->1->2->3->4->4->5->6


from typing import List, Optional
from py.collections.list import ListNode


class Solution:
    def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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

        n = len(lists)

        if not n:
            return None

        i = 0
        j = n - 1

        while j:
            while i < j:
                lists[i] = merge_two_lists(lists[i], lists[j])
                i, j = i+1, j-1
            i = 0

        return lists[0]