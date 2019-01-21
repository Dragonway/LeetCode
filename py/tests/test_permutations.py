import unittest
from py.tests.utils import test
from py import permutations
from py import permutations2


class TestPermutations(unittest.TestCase):

    @test(permutations.Solution.permute)
    def test_permutations(self):
        test([1, 2, 3], result=[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]])
        test([1],       result=[[1]])
        test([],        result=[[]])

    @test(permutations2.Solution.permute_unique)
    def test_permutations(self):
        test([1, 2, 3],     result=[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
        test([1],           result=[[1]])
        test([],            result=[[]])
        test([1, 1, 2],     result=[[1, 1, 2], [1, 2, 1], [2, 1, 1]])
        test([2, 2, 1, 1],  result=[[1,1,2,2],[1,2,1,2],[1,2,2,1],[2,1,1,2],[2,1,2,1],[2,2,1,1]])
