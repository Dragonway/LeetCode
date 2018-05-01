import unittest
from py.tests.utils import test
from py import valid_parentheses as vp


class TestValidParentheses(unittest.TestCase):

    @test(vp.Solution.is_valid)
    def test_valid_parentheses(self) -> None:
        test("()",          result=True)
        test("()[]{}",      result=True)
        test("(]",          result=False)
        test("([)]",        result=False)
        test("{[]}",        result=True)
        test("",            result=True)
        test(")()",         result=False)
        test("(())((())))", result=False)
