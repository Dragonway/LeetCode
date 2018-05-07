# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5


from typing import Optional
from py.collections.list import ListNode


class Solution:
    def remove_elements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new_head = node = None
        while head:
            _next = head.next

            if head.val != val:
                if not node:
                    node = head
                    node.next = None
                    new_head = node
                else:
                    node.next = head
                    node = node.next
                    node.next = None

            head = _next

        return new_head
