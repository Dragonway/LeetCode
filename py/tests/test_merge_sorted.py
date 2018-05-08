import unittest
from py.tests.utils import test
from py.collections.list import List
from py import merge_two_sorted_lists as merge2list
from py import merge_k_sorted_lists as mergeKlist
from py import merge_two_sorted_arrays as merge2array
from py import summary_ranges as sr


class TestMergeSorted(unittest.TestCase):

    @test(merge2list.Solution.merge_two_lists)
    def test_merge_two_sorted_lists(self) -> None:
        test(List([1, 2, 4]).root,  List([1, 3, 4]).root,       result=List([1, 1, 2, 3, 4, 4]).root)
        test(List([1 ,1 ,1]).root,  List([1, 1, 1]).root,       result=List([1, 1, 1, 1, 1, 1]).root)
        test(List([-2, 0, 2]).root, List([-4, -3, -1]).root,    result=List([-4, -3, -2, -1, 0, 2]).root)
        test(List([1, 2, 3]).root,  List([4, 5, 6]).root,       result=List([1, 2, 3, 4, 5, 6]).root)
        test(List([4, 5, 6]).root,  List([1, 2, 3]).root,       result=List([1, 2, 3, 4, 5, 6]).root)
        test(List([4, 5, 6]).root,  List([1, 2]).root,          result=List([1, 2, 4, 5, 6]).root)
        test(List([1, 2, 3]).root,  List([]).root,              result=List([1, 2, 3]).root)
        test(List([]).root,         List([1, 2, 3]).root,       result=List([1, 2, 3]).root)
        test(List([]).root,         List([]).root,              result=List([]).root)

    @test(mergeKlist.Solution.merge_k_lists)
    def test_merge_k_sorted_lists(self) -> None:
        test([List([1, 4, 5]).root, List([1, 3, 4]).root,   List([2, 6]).root],         result=List([1, 1, 2, 3, 4, 4, 5, 6]).root)
        test([List([]).root,        List([-1, 0, 1]).root,  List([8, 10, 154]).root],   result=List([-1, 0, 1, 8, 10, 154]).root)
        test([List([1, 1, 1]).root, List([1, 1, 1]).root,   List([1]).root],            result=List([1, 1, 1, 1, 1, 1, 1]).root)
        test([List([0]).root,       List([-3]).root,        List([5]).root],            result=List([-3, 0, 5]).root)
        test([List([]).root,        List([]).root,          List([8, 9, 11]).root],     result=List([8, 9, 11]).root)
        test([List([]).root,        List([]).root,          List([]).root],             result=List([]).root)

    @unittest.expectedFailure
    @test(merge2array.Solution.merge)
    def test_merge_two_sorted_arrays(self) -> None:
        test([1, 2, 4, 0, 0, 0],    3,  [1, 3, 4],      3,  _1=[1, 1, 2, 3, 4, 4])
        test([1, 1, 1, 1, 1, 1],    3,  [1, 1, 1],      3,  _1=[1, 1, 1, 1, 1, 1])
        test([-2, 0, 2, -1, 0, 1],  3,  [-4, -3, -1],   3,  _1=[-4, -3, -2, -1, 0, 2])
        test([1, 2, 3, 3, 2, 1],    3,  [4, 5, 6],      3,  _1=[1, 2, 3, 4, 5, 6])
        test([4, 5, 6, 0, 0, 0],    3,  [1, 2, 3],      3,  _1=[1, 2, 3, 4, 5, 6])
        test([4, 5, 6, 7, 8],       3,  [1, 2],         2,  _1=[1, 2, 4, 5, 6])
        test([1, 2, 3],             3,  [],             0,  _1=[1, 2, 3])
        test([0, 0, 0],             0,  [1, 2, 3],      3,  _1=[1, 2, 3])
        test([],                    0,  [],             0,  _1=[])

    @test(sr.Solution.summary_ranges)
    def test_summary_ranges(self) -> None:
        test([0, 1, 2, 4, 5, 7],    result=['0->2', '4->5', '7'])
        test([0, 2, 3, 4, 6, 8, 9], result=['0', '2->4', '6', '8->9'])
        test([-3, -2, 0, 1, 2],     result=['-3->-2', '0->2'])
        test([-2, -1, 0, 4, 6],     result=['-2->0', '4', '6'])
        test([-1, 0, 1, 2, 4],      result=['-1->2', '4'])
        test([0, 1, 2, 3, 4, 5],    result=['0->5'])
        test([1],                   result=['1'])
        test([],                    result=[])
