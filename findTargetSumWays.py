#! /usr/bin/python3

def findTargetSumWays(nums, S):
    mem = {}
    def find(arr, index, value, S):
        if index == len(arr):
            return 1 if value == S else 0
        else:
            if (index, value) in mem:
                return mem[(index, value)]
            cur = arr[index]
            add = find(arr, index + 1, value + cur, S)
            sub = find(arr, index + 1, value - cur, S)
            total = add + sub
            mem[(index, value)] = total
            return total
    return find(nums, 0, 0, S)

nums, s = [1,1,1,1,1], 3
expected = 5
actual = findTargetSumWays(nums, s)
print(f"expected {expected}, actual: {actual}")
