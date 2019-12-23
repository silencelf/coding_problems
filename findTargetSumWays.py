#! /usr/bin/python3

from collections import deque

def findTargetSumWays(nums, s):
    nu = deque(nums)
    def search(numbers, sign, current, target):
        if not numbers:
            return 1 if current == target else 0

        value = numbers.popleft()
        if sign == '+':
            current += value
        else:
            current -= value
        plus = search(numbers.copy(), '+', current, target) 
        minus = search(numbers.copy(), '-', current, target) 
        return plus + minus
    return search(nu.copy(), '+', 0, s) + search(nu.copy(), '-', 0, s)

nums, s = [1,1,1,1,1], 3
expected = 5
actual = findTargetSumWays(nums, s)
print(f"expected {expected}, actual: {actual}")
