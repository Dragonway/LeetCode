import unittest
from py.tests.utils import test
from py import remove_duplicates_from_sorted_array as rdfsa


class TestRemoveElements(unittest.TestCase):

    @test(rdfsa.Solution.remove_duplicates)
    def test_remove_duplicates_from_sorted_array(self) -> None:
        test([1, 1, 2],             result=[1, 2])
        test([0,0,1,1,1,2,2,3,3,4], result=[0, 1, 2, 3, 4])
        test([1, 1, 1, 1],          result=[1])
        test([0],                   result=[0])
        test([],                    result=[])