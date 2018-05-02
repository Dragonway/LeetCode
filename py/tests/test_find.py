import unittest
from py.tests.utils import test
from py import find_disappeared_numbers as fdn


class TestFind(unittest.TestCase):

    @test(fdn.Solution.find_disappeared_numbers)
    def test_find_disappeared_numbers(self) -> None:
        test([4, 3, 2, 7, 8, 2, 3, 1],  result=[5, 6])
        test([8, 8, 8, 8, 8, 8, 8, 8],  result=[1, 2, 3, 4, 5, 6, 7])
        test([4, 2, 5, 7, 8, 6, 3, 1],  result=[])
        test([1, 2],                    result=[])
        test([2, 1],                    result=[])
        test([1, 1],                    result=[2])
        test([1],                       result=[])
        test([],                        result=[])
