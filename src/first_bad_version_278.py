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


def isBadVersion(version: int):
    """
    This is a placeholder function, meant to be used by the external unittest
    framework to simulate which one is the first bad version

    :raises: ValueError as this is meant to be patched/mock
    """
    raise ValueError("This function is supposed to be patched in unittest")


class SolutionProblem278:

    def firstBadVersion(self, n: int) -> int:

        # Check corner case of n being 1
        if n == 1:
            return n

        # Check corner case of 1 being the first badVersion
        if isBadVersion(1):
            return 1

        middle = n//2
        start = 1
        end = n
        lastGood = 1

        while True:

            if isBadVersion(middle):
                if lastGood == (middle-1):
                    return middle
                else:
                    end = middle
                    middle = ((end - start)//2) + start

            else:
                lastGood = middle
                start = middle
                candidate = ((end - middle)//2) + start
                if candidate == start:
                    return candidate + 1
                else:
                    middle = candidate
