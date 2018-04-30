import unittest
from typing import List
from bst import BinarySearchTree
from two_sum4 import Solution


class TestTwoSum4(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def _test(self, nums: List[int], target: int, result: bool) -> None:
        with self.subTest(nums=nums, target=target):
            self.assertEqual(self.solution.two_sum4(BinarySearchTree(nums).root, target), result)

    def test_two_sum(self) -> None:
        self._test([5, 3, 6, 2, 4, 7], 9, True)
        self._test([5, 3, 6, 2, 4, 7], 3, False)
        self._test([2, 3, 4, 5, 6, 7], 2, False)
        self._test([2, 3, 4, 5, 6, 7], 7, True)
        self._test([2, 3, 4, 5, 6, 7], 5, True)
        self._test([2, 3, 4, 5, 6, 7], 9, True)
        self._test([2, 3, 4, 5, 6, 7], 13, True)
        self._test([7, 6, 5, 4, 3, 2], 2, False)
        self._test([7, 6, 5, 4, 3, 2], 7, True)
        self._test([7, 6, 5, 4, 3, 2], 5, True)
        self._test([7, 6, 5, 4, 3, 2], 9, True)
        self._test([7, 6, 5, 4, 3, 2], 13, True)
        self._test([0, 1], 1, True)
        self._test([5], 5, False)
        self._test([], 0, False)


if __name__ == '__main__':
    unittest.main()
