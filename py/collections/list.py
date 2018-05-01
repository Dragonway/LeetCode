from typing import List as ListBase, Optional


class ListNode:
    def __init__(self, x: int):
        self.val: int = x
        self.next: Optional[ListNode] = None


class List:
    def __init__(self, elements: Optional[ListBase[int]] = None):
        self.root: Optional[ListNode] = None

        if elements is None:
            return

        for elem in elements:
            self.add(elem)

    def add(self, element: int) -> None:
        if self.root is None:
            self.root = ListNode(element)
            return

        node = self.root
        while node.next is not None:
            node = node.next

        node.next = ListNode(element)
