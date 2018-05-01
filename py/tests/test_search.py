import unittest
from py.tests.utils import test
from py import search_insert_position as sip


class TestSearch(unittest.TestCase):

    @test(sip.Solution.search_insert)
    def test_search_insert_position(self):
        test([1, 3, 5, 6],      5,  result=2)
        test([1, 3, 5, 6],      2,  result=1)
        test([1, 3, 5, 6],      7,  result=4)
        test([1, 3, 5, 6],      0,  result=0)
        test([1, 3, 5, 6, 8],   3,  result=1)
        test([1, 3, 5, 6, 8],   7,  result=4)
        test([],                0,  result=0)