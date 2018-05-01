import unittest
from py.tests.utils import test
from py.collections.bst import BinarySearchTree
from py import two_sum1 as ts1
from py import two_sum2 as ts2
from py import two_sum4 as ts4


class TestTwoSum(unittest.TestCase):

    @test(ts1.Solution.two_sum)
    def test_two_sum1(self) -> None:
        test([2, 7, 11, 15], 9, result=[0, 1])
        test([-1, 0, 9, -5], -6, result=[0, 3])
        test([0, 0], 0, result=[0, 1])

    @test(ts2.Solution.two_sum)
    def test_two_sum2(self) -> None:
        test([2, 7, 11, 15], 9, result=[1, 2])
        test([-1, 0, 9, -5], -6, result=[1, 4])
        test([0, 0], 0, result=[1, 2])

    @test(ts4.Solution.two_sum)
    def test_two_sum4(self) -> None:
        test(BinarySearchTree([5, 3, 6, 2, 4, 7]).root, 9, result=True)
        test(BinarySearchTree([5, 3, 6, 2, 4, 7]).root, 3, result=False)
        test(BinarySearchTree([2, 3, 4, 5, 6, 7]).root, 2, result=False)
        test(BinarySearchTree([2, 3, 4, 5, 6, 7]).root, 7, result=True)
        test(BinarySearchTree([2, 3, 4, 5, 6, 7]).root, 5, result=True)
        test(BinarySearchTree([2, 3, 4, 5, 6, 7]).root, 9, result=True)
        test(BinarySearchTree([2, 3, 4, 5, 6, 7]).root, 13, result=True)
        test(BinarySearchTree([7, 6, 5, 4, 3, 2]).root, 2, result=False)
        test(BinarySearchTree([7, 6, 5, 4, 3, 2]).root, 7, result=True)
        test(BinarySearchTree([7, 6, 5, 4, 3, 2]).root, 5, result=True)
        test(BinarySearchTree([7, 6, 5, 4, 3, 2]).root, 9, result=True)
        test(BinarySearchTree([7, 6, 5, 4, 3, 2]).root, 13, result=True)
        test(BinarySearchTree([0, 1]).root, 1, result=True)
        test(BinarySearchTree([5]).root, 5, result=False)
        test(BinarySearchTree([]).root, 0, result=False)


if __name__ == '__main__':
    unittest.main()
