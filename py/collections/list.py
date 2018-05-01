from typing import List as ListBase, Optional, Union


class ListNode:
    def __init__(self, x: int):
        self.val: int = x
        self.next: Optional[ListNode] = None


class List:
    def __init__(self, elements: Optional[Union[ListBase[int], ListNode]] = None):
        self.root: Optional[ListNode] = None

        if elements is None:
            return

        if isinstance(elements, ListNode):
            self.root = elements
        else:
            for elem in elements:
                self.add(elem)

    def __eq__(self, other: 'List'):
        lhs = self.root
        rhs = other.root

        while lhs is not None and rhs is not None:
            if lhs.val != rhs.val:
                return False

            lhs = lhs.next
            rhs = rhs.next

        return lhs is rhs

    def add(self, element: int) -> None:
        if self.root is None:
            self.root = ListNode(element)
            return

        node = self.root
        while node.next is not None:
            node = node.next

        node.next = ListNode(element)
