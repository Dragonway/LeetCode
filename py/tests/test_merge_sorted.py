import unittest
from py.tests.utils import test
from py.collections.list import List
from py import merge_two_sorted_lists as merge2list


class TestMergeSorted(unittest.TestCase):

    @test(merge2list.Solution.merge_two_lists)
    def test_merge_two_sorted_lists(self) -> None:
        test(List([1, 2, 4]).root, List([1, 3, 4]).root, result=List([1, 1, 2, 3, 4, 4]).root)
        test(List([1 ,1 ,1]).root, List([1, 1, 1]).root, result=List([1, 1, 1, 1, 1, 1]).root)
        test(List([-2, 0, 2]).root, List([-4, -3, -1]).root, result=List([-4, -3, -2, -1, 0, 2]).root)
        test(List([1, 2, 3]).root, List([4, 5, 6]).root, result=List([1, 2, 3, 4, 5, 6]).root)
        test(List([4, 5, 6]).root, List([1, 2, 3]).root, result=List([1, 2, 3, 4, 5, 6]).root)
        test(List([4, 5, 6]).root, List([1, 2]).root, result=List([1, 2, 4, 5, 6]).root)
        test(List([1, 2, 3]).root, List([]).root, result=List([1, 2, 3]).root)
        test(List([]).root, List([1, 2, 3]).root, result=List([1, 2, 3]).root)
        test(List([]).root, List([]).root, result=List([]).root)
