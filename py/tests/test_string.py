import unittest
from py.tests.utils import test
from py import implement_strstr as strstr


class TestString(unittest.TestCase):

    @test(strstr.Solution.str_str)
    def test_strstr(self) -> None:
        test("hello",   "ll",   result=2)
        test("aaaaa",   "bba",  result=-1)
        test("abbaba",  "ab",   result=0)
        test("abbaba",  "aba",  result=3)
        test("aaababa", "aaba", result=1)
        test("test",    "",     result=0)
        test("",        "test", result=-1)
        test("",        "",     result=0)
