#!/usr/bin/env python3

# Given a string s, return the longest palindromic substring in s.
#
#  Example 1:
#
#     Input: s = "babad"
#     Output: "bab"
#     Explanation: "aba" is also a valid answer.
#
#  Example 2:
#
#     Input: s = "cbbd"
#     Output: "bb"
#
# Constraints:
#     1 <= s.length <= 1000
#    s consist of only digits and English letters.
#
# Definition
# class Solution:
#         def longestPalindrome(self, s: str) -> str:
#             pass

from src.longest_palindromic_substring_5 import Solution


class TestSolutionProblem704(unittest.TestCase):

    # This is run before calling this test case
    def setUp(self):

        self.solution = Solution()

    def test_custom(self):
        """
        Test simple inputs
        """

        test_str = "banana"
        expected = "anana"

        result = self.solution()
        self.assertEqual(expected, result)

