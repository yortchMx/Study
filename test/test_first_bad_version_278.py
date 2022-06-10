#!/usr/bin/env python3

# First Bad Version 278
# You are a product manager and currently leading a team to develop a new
# product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the
# versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the
# first bad one, which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which returns whether
# version is bad. Implement a function to find the first bad version.
# You should minimize the number of calls to the API.
#
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
#
# Example 1:
#
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
# Example 2:
#
# Input: n = 1, bad = 1
# Output: 1
#
# Constraints:
#
# 1 <= bad <= n <= 231 - 1

# Solution definition
# class Solution:
#     def firstBadVersion(self, n: int) -> int:

import random
import unittest
from unittest.mock import MagicMock, patch
from src.first_bad_version_278 import SolutionProblem278


class TestSolutionProblem278(unittest.TestCase):

    # unittest setup
    def setUp(self):
        self.solution = SolutionProblem278()
        self.BAD_SMALLEST = 1
        self.BAD_BIGGEST = 230

    @patch("src.first_bad_version_278.isBadVersion")
    def test_custom(self, magicIsBadVersion: MagicMock):
        """
        Test simple inputs
        """

        # Declare a custom first bad version
        first_bad_version = 2

        # Create a side effect helper function
        # The isBadVersion in the solution class is patched to be driven
        # by this simple function
        def side_effect_func(version):
            if version >= first_bad_version:
                return True

        # Declare arbitary size of n (within contraints)
        n = 75

        magicIsBadVersion.side_effect = side_effect_func
        result = self.solution.firstBadVersion(n)
        self.assertEqual(result, first_bad_version)

    @patch("src.first_bad_version_278.isBadVersion")
    def run_case_parametrized(self, magicIsBadVersion: MagicMock):
        """
        Randomize a parametrized test to stress method under test

        Constraints:
        1 <= bad <= n <= 231 - 1
        self.BAD_SMALLEST = 1
        self.BAD_BIGGEST = 230
        """
        # Define number of randome subtest
        number_of_tests = 50

        for i in range(number_of_tests):

            # Generate random first bad version within limits
            first_bad_version = random.randint(
                    self.BAD_SMALLEST, self.BAD_BIGGEST)

            # Create a side effect helper function
            # The isBadVersion in the solution class is patched to be driven
            # by this simple function
            def side_effect_func(version):
                if version >= first_bad_version:
                    return True

            # Declare random size of n (within contraints)
            n = random.randint(
                    self.BAD_SMALLEST, first_bad_version)

            magicIsBadVersion.side_effect = side_effect_func
            self.assertEqual(
                    self.solution.firstBadVersion(n), first_bad_version)

    def runTest(self):
        """
        Randomize a parametrized test to stress method under test
        """
        self.test_custom()
        self.run_case_parametrized()
