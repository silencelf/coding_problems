#!/user/bin/python

"""
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]


Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
"""

class Solution:
    def plusOne(self, digits):
        result = []
        up = 1
        for d in reversed(digits):
            current = d + up
            if current < 10:
                result.append(current)
                up = 0
            else:
                this = (current) % 10
                up = current // 10
                result.append(this)
        if up > 0:
            result.append(up)
        return list(reversed(result))


testSuites = [
    ([1,2,3], [1,2,4]),
    ([4,3,2,1], [4,3,2,2]),
    ([0], [1]),
    ([8, 9], [9, 0]),
    ([9, 9], [1, 0, 0])
]

s = Solution()
for case in testSuites:
    ret = s.plusOne(case[0])
    print(ret)
    if ret == case[1]:
        print('case passed.')
    else:
        print(f'case {case[0]} failed.')
