import os
import sys

from test_base import TestBase

current_dir = os.path.dirname(__file__)
module_dir = os.path.join(current_dir, "..")
sys.path.append(module_dir)

from exercise.greatest_common_divisor import gcdOfStrings


class TestgreatestCommonDivisor(TestBase):
    """
    For two strings s and t, we say "t divides s" 
    if and only if s = t + t + t + ... + t + t 
    (i.e., t is concatenated with itself one or more times).

    Given two strings str1 and str2, return the largest 
    string x such that x divides both str1 and str2."""
    def test_example1(self):
        str1 = "ABCABC"
        str2 = "ABC"
        expected = "ABC"
        self.assertEqual(gcdOfStrings(str1, str2), expected)

    def test_example2(self):
        str1 = "ABABAB"
        str2 = "ABAB"
        expected = "AB"
        self.assertEqual(gcdOfStrings(str1, str2), expected)

    def test_example3(self):
        str1 = "LEET"
        str2 = "CODE"
        expected = ""
        self.assertEqual(gcdOfStrings(str1, str2), expected)