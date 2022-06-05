#!/usr/bin/env python3

# 704. Binary Search
# Given an array of integers nums which is sorted in ascending order, and an
# integer target, write a function to search target in nums. If target exists,
# then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
#     Input: nums = [-1,0,3,5,9,12], target = 9
#     Output: 4
#     Explanation: 9 exists in nums and its index is 4

# Example 2:
#     Input: nums = [-1,0,3,5,9,12], target = 2
#     Output: -1
#     Explanation: 2 does not exist in nums so return -1
#
# Constraints:
#     1 <= nums.length <= 104
#     -104 < nums[i], target < 104
#     All the integers in nums are unique.
#     nums is sorted in ascending order.
#

# Solution definition
# class SolutionProblem704:
#   search(self, nums: List[int], target: int) -> int:

import random
import unittest
from binary_search_704 import SolutionProblem704


class TestSolutionProblem704(unittest.TestCase):

    # This is run before calling this test case
    def setUp(self):

        self.solution = SolutionProblem704()
        self.NUMS_LENGTH_MAX = 104
        self.NUMS_LENGTH_MIN = 1
        self.NUMS_SMALLEST = -140
        self.NUMS_BIGGEST = 140

    def test_custom(self):
        """
        Test simple inputs
        """

        nums = [-3, 3, 4, 8, 9, 32]
        target = 2
        expected = -1
        self.assertEqual(expected, self.solution.search(nums, target))

    def test_parametrized(self, positive: bool):
        """
        Randomize a parametrized test to stress method under test
        """
        # Define number of randome subtest
        number_of_tests = 50

        for i in range(number_of_tests):

            # Generate random nums list
            nums_lenght = random.randint(
                    self.NUMS_LENGTH_MIN, self.NUMS_LENGTH_MAX)
            nums = random.sample(
                population=range(self.NUMS_SMALLEST, self.NUMS_BIGGEST),
                k=nums_lenght)

            # Make sure nums is sorted
            nums.sort()

            # Create a random integer target
            target = int(random.random() * 300)

            if target in nums:
                expected = nums.index(target)
            else:
                expected = -1

            with self.subTest(
                    "Incorrect result", target=target,
                    expected=expected):
                self.assertEqual(expected, self.solution.search(nums, target))
