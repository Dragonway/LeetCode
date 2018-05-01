import unittest
from py.tests.utils import test
from py import remove_duplicates_from_sorted_array as rdfsa
from py import remove_element as re


# TODO: Need some utils for testing in-place solutions
class TestRemoveElements(unittest.TestCase):

    @test(rdfsa.Solution.remove_duplicates)
    def test_remove_duplicates_from_sorted_array(self) -> None:
        test([1, 1, 2],             result=[1, 2])
        test([0,0,1,1,1,2,2,3,3,4], result=[0, 1, 2, 3, 4])
        test([1, 1, 1, 1],          result=[1])
        test([0],                   result=[0])
        test([],                    result=[])

    @test(re.Solution.remove_element)
    def test_remove_element(self) -> None:
        test([3, 2, 2, 3],              3,  result=[2, 2])
        test([0, 1, 2, 2, 3, 0, 4, 2],  2,  result=[0, 1, 4, 0, 3])
        test([1, 1, 1],                 1,  result=[])
        test([3, 4],                    0,  result=[3, 4])
        test([1],                       0,  result=[1])
        test([0],                       0,  result=[])
        test([],                        0,  result=[])
