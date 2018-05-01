import unittest
from py.tests.utils import test
from py import array_partition1 as ap1


class TestSum(unittest.TestCase):

    @test(ap1.Solution.array_pair_sum)
    def test_array_pair_sum1(self) -> None:
        test([1, 4, 3, 2],          result=4)
        test([0, 0],                result=0)
        test([0, 0, 0, 0, 0, 0],    result=0)
        test([4, 2, -2, -4],        result=-2)
        test([1, -1, -1, 1],        result=0)
