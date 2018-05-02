import unittest
from py.tests.utils import test
from py import find_disappeared_numbers as fdn
from py import max_area_of_island as maoi


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

    @test(maoi.Solution.max_area_of_island)
    def test_max_area_of_island(self) -> None:
        test([[0, 0, 0, 0, 0]],     result=0)

        test([[0, 0, 1, 1, 1],
              [0, 0, 0, 0, 0]],     result=3)

        test([[0, 0, 1, 0, 0],
              [1, 1, 0, 0, 0]],     result=2)

        test([[0, 0, 1, 0, 0],
              [1, 0, 1, 1, 0],
              [1, 1, 0, 0, 0]],     result=3)

        test([[1, 1, 0, 0, 0],
              [1, 1, 0, 0, 1],
              [0, 0, 1, 1, 0],
              [1, 0, 0, 1, 0],
              [0, 0, 0, 0, 0]],     result=4)

        test([[0, 0, 1, 0, 1],
              [1, 1, 1, 0, 1],
              [1, 0, 0, 1, 1],
              [1, 0, 0, 1, 0],
              [1, 1, 1, 1, 0]],     result=15)

        test([[0, 0, 1, 0, 1],
              [1, 1, 1, 1, 1],
              [1, 0, 1, 1, 1],
              [1, 0, 0, 1, 0],
              [1, 1, 1, 1, 0]],     result=17)

        test([[1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1]],     result=25)

        test([[1, 0, 1, 0, 1],
              [0, 1, 0, 1, 0],
              [1, 0, 1, 0, 1],
              [0, 1, 0, 1, 0],
              [1, 0, 1, 0, 1]], result=1)

        test([[1]],                 result=1)
