from typing import List, Optional


class TreeNode:
    def __init__(self, x: int):
        self.val: int = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class BinarySearchTree:
    def __init__(self, elements: Optional[List[int]] = None):
        self.root: Optional[TreeNode] = None

        if elements is None:
            return

        for elem in elements:
            self.add(elem)

    def add(self, element: int) -> None:
        if self.root is None:
            self.root = TreeNode(element)
            return

        node = self.root

        while True:
            if element > node.val:
                if node.right is None:
                    node.right = TreeNode(element)
                    return

                node = node.right
            elif element < node.val:
                if node.left is None:
                    node.left = TreeNode(element)
                    return

                node = node.left
            else:
                return
