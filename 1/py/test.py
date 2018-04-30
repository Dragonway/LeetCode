import unittest
from typing import List
from two_sum import Solution


class TestTwoSum(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def _test(self, nums: List[int], target: int, result: List[int]) -> None:
        with self.subTest(nums=nums, target=target):
            self.assertEqual(self.solution.two_sum(nums, target), result)

    def test_two_sum(self) -> None:
        self._test([2, 7, 11, 15], 9, [0, 1])
        self._test([-1, 0, 9, -5], -6, [0, 3])
        self._test([0, 0], 0, [0, 1])


if __name__ == '__main__':
    unittest.main()