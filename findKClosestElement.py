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
Absolute value of elements in the array and x will not exceed 104
"""

class Solution:
    def findClosestElements(self, arr, k, x):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        # End condition left == right
#       if left != len(arr) and arr[left] == x:
#           return left
        return -1

s = Solution()

# example 1
arr = [1,2,3,4,5]
k = 4
x = 3
expected = [1,2,3,4]

index = 0
while index < len(arr):
    result = s.findClosestElements(arr, k, arr[index])
    print(result)
    index += 1
