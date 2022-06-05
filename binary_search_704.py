#!/usr/bin/env python3

# 704. Binary Search
# Given an array of integers nums which is sorted in ascending order, and an
# integer target, write a function to search target in nums. If target exists,
# then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        index = -1

        # Get middle and end
        end = len(nums) - 1
        middle = len(nums)/2

        while True:

            if nums[middle] == target:
                return middle

            elif nums[middle] < target:
                candidate = ((end - middle)/2) + middle

                # all good
                if middle != candidate:
                    end
                    middle = candidate
                else:   # reached end
                    break
            else:
                candidate = (middle/2)

                # all good
                if middle != candidate:
                    middle = candidate
                else:   # reached end
                    break
        return index
