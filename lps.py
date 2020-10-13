#! /usr/bin/python

"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
class Solution:
    lo = 0
    longest = 0
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            self.extend(s, i, i)
            self.extend(s, i, i + 1)
        return s[self.lo:self.lo + self.longest]

    def extend(self, s, j, k):
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1
        if k - j - 1 > self.longest:
            self.lo = j + 1
            self.longest = k -j - 1
# tests
sol = Solution()
s = "babad"
ret = sol.longestPalindrome(s)
print(ret)
s = "aaabbbb"
ret = sol.longestPalindrome(s)
print(ret)
s = "aa"
ret = sol.longestPalindrome(s)
print(ret)
