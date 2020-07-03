#! /usr/bin/python3

values = [60, 100, 120, 130]
weights = [10, 20, 30, 30]
W = 50

"" naive version,O(2^n)
def knapsack(n, s):
    print(f'n = {n}, s = {s}')
    w = weights[n]
    v = values[n]
    print(f'w = {w}, v = {v}')
    if n == -1 or s == 0:
        return 0
    if w > s:
        return knapsack(n - 1, s)
    else:
        v1 = knapsack(n - 1, s)
        v2 = v + knapsack(n - 1, s - w)
        return max(v1, v2)

result = knapsack(len(values) - 1, W)
print(f'knapset result: {result}')
