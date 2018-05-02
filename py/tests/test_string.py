import unittest
from py.tests.utils import test
from py import implement_strstr as strstr
from py import longest_substr_without_repeats as lswr


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

    @test(lswr.Solution.length_of_longest_substr)
    def test_length_of_longest_substr(self) -> None:
        test('abcabcbb',    result=3)
        test('bbbbb',       result=1)
        test('pwwkew',      result=3)
        test('abcadcbb',    result=4)
        test('abcdefa',     result=6)
        test('abcdefg',     result=7)
        test('aab',         result=2)
        test('a',           result=1)
        test('',            result=0)
