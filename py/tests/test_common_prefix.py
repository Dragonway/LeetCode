import unittest
from typing import List
from py.tests.utils import solution
from py import longest_common_prefix as lcp


class TestCommonPrefix(unittest.TestCase):

    def _test(self, solution: lcp.Solution, strs: List[str], result: str) -> None:
        with self.subTest(strs=strs):
            self.assertEqual(solution.longest_common_prefix(strs), result)

    @solution(lcp)
    def test_longest_common_prefix(self) -> None:
        self._test(solution, ["flower","flow","flight"], "fl")
        self._test(solution, ["dog","racecar","car"], "")
        self._test(solution, ["flower", "flow", "slide"], "")
        self._test(solution, ["flower", "flow", ""], "")
        self._test(solution, ["flower", "flow"], "flow")
        self._test(solution, [""], "")
        self._test(solution, [], "")
