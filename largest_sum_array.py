#!/bin/python
"""
Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-2147483647]
Output: -2147483647


Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1

[-2,1,-3,4,-1,2,1,-5,4]

[-2,1,-3,(4,-1,2,1),-5,4]


"""

class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        for i in range(1, len(nums)):
            if nums[i -1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)

    def maxSubArray_naive(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        m = None
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                s = sum(nums[i:j])
                if m == None or m < s:
                    m = s
        return m

def tests():
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    expected =  6
    ret = s.maxSubArray(nums)
    print(f'input {nums}, expected: {expected}, actual: {ret}')

    nums = [1]
    expected =  1
    ret = s.maxSubArray(nums)
    print(f'input {nums}, expected: {expected}, actual: {ret}')

    nums = [0]
    expected =  0
    ret = s.maxSubArray(nums)
    print(f'input {nums}, expected: {expected}, actual: {ret}')

    nums = [-1]
    expected =  -1
    ret = s.maxSubArray(nums)
    print(f'input {nums}, expected: {expected}, actual: {ret}')

    nums = [-2147483647]
    expected =  -2147483647
    ret = s.maxSubArray(nums)
    print(f'input {nums}, expected: {expected}, actual: {ret}')

tests()
