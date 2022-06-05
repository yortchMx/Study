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

from typing import List


class SolutionProblem704:

    def search(self, nums: List[int], target: int) -> int:

        # Declare value to return, if we don't fin target we should return
        # -1
        index = -1

        # Get middle and end
        end = len(nums)
        middle = len(nums)//2

        # Continously iterate
        while True:

            # Compare the current value at the middle of nums with target
            if nums[middle] == target:
                return middle

            # Search on the first half of nums instead
            elif nums[middle] < target:
                candidate = ((end - middle)//2) + middle

                # All good
                if middle != candidate:
                    middle = candidate

                # Reached end
                else:
                    break
            else:
                candidate = (middle//2)

                # All good
                if middle != candidate:
                    end = middle
                    middle = candidate

                # Reached end
                else:
                    break
        return index
