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
        if len(arr) == 0:
            return []
        index = self.binSearch(arr, x)
        result = self.findClosest(arr, k, x, index)
        return result

    def binSearch(self, arr, x): 
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return mid

    def findClosest(self, arr, k, x, index):
        result = []
        if arr[index] == x:
            result.append(arr[index])
            i = index - 1
            j = index + 1
            k = k - 1
        else:
            i = index - 1
            j = index
        while k > 0:
            left = arr[i] - x
            right = arr[j] - x
            if i > -1 and left <= right:
                print('left')
                result.append(arr[i])
                i -= 1
            elif j < len(arr):
                print('right')
                result.append(arr[j])
                j += 1
            k -= 1
        return result

s = Solution()

# example 1
arr = [1,2,3,4,5]
k = 4
x = 3
expected = [1,2,3,4]

# index = 0
# while index < len(arr):
#     result = s.findClosestElements(arr, k, arr[index])
#     print(result)
#     index += 1

result = s.findClosestElements(arr, k, 3)
print(result)

result = s.findClosestElements(arr, 3, 4)
print(result)

result = s.findClosestElements(arr, 3, 2.5)
print(result)
