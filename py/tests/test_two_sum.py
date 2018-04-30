import unittest
from typing import List
from py.collections.bst import BinarySearchTree
from py import two_sum1 as ts1
from py import two_sum2 as ts2
from py import two_sum4 as ts4


class TestTwoSum(unittest.TestCase):

    def _test_list(self, solution, nums: List[int], target: int, result: List[int]) -> None:
        with self.subTest(nums=nums, target=target):
            self.assertEqual(solution.two_sum(nums, target), result)

    def test_two_sum1(self) -> None:
        solution = ts1.Solution()

        self._test_list(solution, [2, 7, 11, 15], 9, [0, 1])
        self._test_list(solution, [-1, 0, 9, -5], -6, [0, 3])
        self._test_list(solution, [0, 0], 0, [0, 1])

    def test_two_sum2(self) -> None:
        solution = ts2.Solution()

        self._test_list(solution, [2, 7, 11, 15], 9, [1, 2])
        self._test_list(solution, [-1, 0, 9, -5], -6, [1, 4])
        self._test_list(solution, [0, 0], 0, [1, 2])

    def _test_bst(self, solution, nums: List[int], target: int, result: bool) -> None:
        with self.subTest(nums=nums, target=target):
            self.assertEqual(solution.two_sum(BinarySearchTree(nums).root, target), result)

    def test_two_sum4(self) -> None:
        solution = ts4.Solution()

        self._test_bst(solution, [5, 3, 6, 2, 4, 7], 9, True)
        self._test_bst(solution, [5, 3, 6, 2, 4, 7], 3, False)
        self._test_bst(solution, [2, 3, 4, 5, 6, 7], 2, False)
        self._test_bst(solution, [2, 3, 4, 5, 6, 7], 7, True)
        self._test_bst(solution, [2, 3, 4, 5, 6, 7], 5, True)
        self._test_bst(solution, [2, 3, 4, 5, 6, 7], 9, True)
        self._test_bst(solution, [2, 3, 4, 5, 6, 7], 13, True)
        self._test_bst(solution, [7, 6, 5, 4, 3, 2], 2, False)
        self._test_bst(solution, [7, 6, 5, 4, 3, 2], 7, True)
        self._test_bst(solution, [7, 6, 5, 4, 3, 2], 5, True)
        self._test_bst(solution, [7, 6, 5, 4, 3, 2], 9, True)
        self._test_bst(solution, [7, 6, 5, 4, 3, 2], 13, True)
        self._test_bst(solution, [0, 1], 1, True)
        self._test_bst(solution, [5], 5, False)
        self._test_bst(solution, [], 0, False)


if __name__ == '__main__':
    unittest.main()
