#!/usr/bin/env python3

# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not
# use the same element twice.
#
# You can return the answer in any order.
# Example 1:
#
#     Input: nums = [2,7,11,15], target = 9
#     Output: [0,1]
#     Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
#
#     Input: nums = [3,2,4], target = 6
#     Output: [1,2]
#
# Example 3:
#
#     Input: nums = [3,3], target = 6
#     Output: [0,1]
#
# Constraints:
#
#          2 <= nums.length <= 104
#          -109 <= nums[i] <= 109
#          -109 <= target <= 109
#          Only one valid answer exists.
#
# Follow-up: Can you come up with an algorithm that is less
# than O(n2) time complexity?

# Defintion
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
#        pass

import unittest
from src.two_sum_1 import SolutionProblem1


class TestSolutionProblem1(unittest.TestCase):

    # This is run before calling this test case
    def setUp(self):

        self.solution = SolutionProblem1()
        self.NUMS_LENGTH_MAX = 104
        self.NUMS_LENGTH_MIN = 1
        self.NUMS_SMALLEST = -140
        self.NUMS_BIGGEST = 140

    def test_custom(self):
        """
        Test simple inputs
        """

        nums = [2,7,11,15]
        target = 9
        expected = [0, -1]
        # Add the sort at the end to compare with a sorted expected list, as
        # the instructions mention that order doesn't matter
        self.assertEqual(expected, self.solution.twoSum(nums, target).sort())

    def run_case_parametrized(self):
        """
        Randomize a parametrized test to stress method under test
        """
        raise NotImplementedError

    def runTest(self):
        """
        Randomize a parametrized test to stress method under test
        """

        self.test_custom()
