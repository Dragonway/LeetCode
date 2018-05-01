import unittest
from py.tests.utils import test
from py import longest_common_prefix as lcp


class TestCommonPrefix(unittest.TestCase):

    @test(lcp.Solution.longest_common_prefix)
    def test_longest_common_prefix(self) -> None:
        test(["flower","flow","flight"],    result="fl")
        test(["dog","racecar","car"],       result="")
        test(["flower", "flow", "slide"],   result="")
        test(["flower", "flow", ""],        result="")
        test(["flower", "flow"],            result="flow")
        test([""],                          result="")
        test([],                            result="")
