import os
import sys

from test_base import TestBase

current_dir = os.path.dirname(__file__)
module_dir = os.path.join(current_dir, "..")
sys.path.append(module_dir)

from exercise.kids_with_candies import kids_with_candies


class TestKidsWithCandies(TestBase):
    """
    There are n kids with candies. You are given an integer array candies, 
    where each candies[i] represents the number of candies the ith kid has, 
    and an integer extraCandies, denoting the number of extra candies that you have.

    Return a boolean array result of length n, 
    where result[i] is true if, after giving the ith kid all the extraCandies, 
    they will have the greatest number of candies among all the kids, or false otherwise.

    Note that multiple kids can have the greatest number of candies.
    """
    def test_example1(self):
        str1 = [2,3,5,1,3]
        str2 = 3
        expected = [True, True, True, False, True]
        self.assertEqual(kids_with_candies(str1, str2), expected)

    def test_example2(self):
        str1 = [4,2,1,1,2]
        str2 = 1
        expected = [True, False, False, False, False]
        self.assertEqual(kids_with_candies(str1, str2), expected)

    def test_example3(self):
        str1 = [12,1,12]
        str2 = 10
        expected = [True, False, True]
        self.assertEqual(kids_with_candies(str1, str2), expected)