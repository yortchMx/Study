#!/usr/bin/env python3

# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
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
import random
from src.two_sum_1 import SolutionProblem1


class TestSolutionProblem1(unittest.TestCase):

    # This is run before calling this test case
    def setUp(self):

        self.solution = SolutionProblem1()
        self.NUMS_LENGTH_MAX = 104
        self.NUMS_LENGTH_MIN = 2
        self.NUMS_SMALLEST = -109
        self.NUMS_BIGGEST = 109
        self.TARGET_SMALLEST = -109
        self.TARGET_BIGGEST = 109

    def test_custom(self):
        """
        Test simple inputs
        """

        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        # Add the sort at the end to compare with a sorted expected list, as
        # the instructions mention that order doesn't matter
        self.assertEqual(expected, sorted(self.solution.twoSum(nums, target)))

    def run_case_parametrized(self):
        """
        Randomize a parametrized test to stress method under test
        Constraints:

              2 <= nums.length <= 104
              -109 <= nums[i] <= 109
              -109 <= target <= 109
              Only one valid answer exists.
        """
        # Define number of randome subtest
        number_of_tests = 50

        for i in range(number_of_tests):

            # Generate random nums list within size limits
            nums_lenght = random.randint(
                    self.NUMS_LENGTH_MIN, self.NUMS_LENGTH_MAX)
            nums = random.sample(
                population=range(self.NUMS_LENGTH_MIN, self.NUMS_LENGTH_MAX),
                k=nums_lenght)

            # Generate two random non equal index of nums
            test_index_1 = random.randint(
                0, nums_lenght)

            # This will be slow for small nums.length, will look for
            # alternatives later, but should not lock as minimum size is 2
            while True:
                test_index_2 = random.randint(
                    0, nums_lenght)
                if test_index_1 != test_index_2:
                    break

            target = nums[test_index_1] + nums[test_index_2]

            self.assertEqual(
                self.solution.twoSum(nums, target), [test_index_1,
                    test_index_2])

    def runTest(self):
        """
        Randomize a parametrized test to stress method under test
        """

        self.test_custom()
        self.parametrized()
