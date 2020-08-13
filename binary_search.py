#! /usr/bin/python

def binary_search(arr, start, end, i):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == i:
        return mid
    elif arr[mid] < i:
        start = mid + 1
    else:
        end = mid - 1
    return binary_search(arr, start, end, i)

# arr = [1, 3, 8, 12 , 15, 16, 44, 56, 70, 100]
# start, end = 0, len(arr) - 1
# index = binary_search(arr, start, end, 70)
# print(index)

arr = [i for i in range(1000000)]
start, end = 0, len(arr) - 1
index = binary_search(arr, start, end, 1010000)
print(index)
