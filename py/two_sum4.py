# Given a Binary Search Tree and a target number,
# return true if there exist two elements in the BST such that their sum is equal to the given target.
#
# Example 1:
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 9
#
# Output: True
#
# Example 2:
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 28
#
# Output: False


from typing import List
from py.collections.bst import TreeNode


class Solution:
    def left_leaf(self, node: TreeNode, stack: List[TreeNode]) -> TreeNode:
        while node.left is not None:
            stack.append(node)
            node = node.left

        return node

    def right_leaf(self, node: TreeNode, stack: List[TreeNode]) -> TreeNode:
        while node.right is not None:
            stack.append(node)
            node = node.right

        return node

    def two_sum(self, root: TreeNode, k: int) -> bool:
        if root is None or (root.left is None and root.right is None):
            return False

        left_stack = []
        left = self.left_leaf(root, left_stack)

        right_stack = []
        right = self.right_leaf(root, right_stack)

        while left is not right:
            sum = left.val + right.val

            if sum == k:
                return True
            elif sum < k:
                if left.right is not None:
                    left = self.left_leaf(left.right, left_stack)
                else:
                    left = left_stack.pop()
            else:
                if right.left is not None:
                    right = self.right_leaf(right.left, right_stack)
                else:
                    right = right_stack.pop()

        return False
