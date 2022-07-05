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

class Solution:

        def longestPalindrome(self, s: str) -> str:

            size = len(s)

            if size == 1:
                return(s)
            elif size == 2:
                return s[0]

            previous = s[0]
            stack = [previous]
            for letter in s[2:]:

                print(f"pusshing {letter}")

                if previous == letter:
                    peak = True

                else:
                    previous =+ 1
                    stack.append(letter)


            return s
