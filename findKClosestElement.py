#! /usr/bin/python

"""
Given a sorted array arr, two integers k and x, find the k closest elements 
to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.


Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 10^4
Absolute value of elements in the array and x will not exceed 10^4
"""

class Solution:
    def findClosestElements(self, arr, k, x):
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left: left + k]

s = Solution()

# example 1
arr = [1,2,3,4,5]
k = 4
x = 3
expected = [1,2,3,4]

result = s.findClosestElements(arr, k, 3)
print(result)

result = s.findClosestElements(arr, 3, 4)
print(result)

result = s.findClosestElements(arr, 3, 2.5)
print(result)
