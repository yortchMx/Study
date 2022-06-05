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

import unittest
from binary_search_704 import SolutionProblem704


class TestSolutionProblem704(unittest.TestCase):

    # This is run before calling this test case
    def setUp(self):

        self.solution = SolutionProblem704()

    def test_custom(self):
        """
        Test simple inputs
        """

        nums = [-3, 3, 4, 8, 9, 32]
        target = 2
        expected = -1
        self.assertEqual(expected, self.solution.search(nums, target))
