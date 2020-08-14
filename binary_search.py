#! /usr/bin/python

import random

def binary_search(arr, i):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == i:
            return mid
        elif arr[mid] < i:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# arr = [1, 3, 8, 12 , 15, 16, 44, 56, 70, 100]
# start, end = 0, len(arr) - 1
# index = binary_search(arr, start, end, 70)
# print(index)

arr = [i for i in range(1000000)]

for i in range(10):
    num = random.randrange(2000000)
    index = binary_search(arr, num)
    print(f'find {num}, result = {index}')
