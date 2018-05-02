import unittest
from py.tests.utils import test
from py.collections.list import List
from py import array_partition1 as ap1
from py import add_two_numbers as add2nums
from py import add_two_numbers2 as add2nums2


class TestSum(unittest.TestCase):

    @test(ap1.Solution.array_pair_sum)
    def test_array_pair_sum1(self) -> None:
        test([1, 4, 3, 2],          result=4)
        test([0, 0],                result=0)
        test([0, 0, 0, 0, 0, 0],    result=0)
        test([4, 2, -2, -4],        result=-2)
        test([1, -1, -1, 1],        result=0)

    @test(add2nums.Solution.add_two_numbers)
    def test_add_two_numbers(self) -> None:
        test(List([2, 4, 3]).root,  List([5, 6, 4]).root,       result=List([7, 0, 8]).root)
        test(List([2, 4, 3]).root,  List([0]).root,             result=List([2, 4, 3]).root)
        test(List([0]).root,        List([5, 6, 4]).root,       result=List([5, 6, 4]).root)
        test(List([1, 1, 1]).root,  List([2, 3]).root,          result=List([3, 4, 1]).root)
        test(List([1, 1, 1]).root,  List([9, 8, 8, 9]).root,    result=List([0, 0, 0, 0, 1]).root)
        test(List([5]).root,        List([6]).root,             result=List([1, 1]).root)
        test(List([0]).root,        List([0]).root,             result=List([0]).root)
