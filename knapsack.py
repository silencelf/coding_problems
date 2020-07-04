#! /usr/bin/python3

values = [60, 100, 120, 130]
weights = [10, 20, 30, 30]
W = 50
memo = {}

def knapsack(n, s):
    print(memo)
    print(f'n = {n}, s = {s}')
    w = weights[n]
    v = values[n]
    #print(f'w = {w}, v = {v}')
    if (n, s) in memo:
        print('found in memo')
        return memo[(n, s)]
    f = 0
    if n == -1 or s == 0:
        memo[(n, s)] = f
        return f
    if w > s:
        f = knapsack(n - 1, s)
    else:
        v1 = knapsack(n - 1, s)
        v2 = v + knapsack(n - 1, s - w)
        f =  max(v1, v2)
    memo[(n, s)] = f
    return f

result = knapsack(len(values) - 1, W)
print(f'knapset result: {result}')
