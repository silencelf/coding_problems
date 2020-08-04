#! /usr/bin/python

values = [60, 100, 120, 130]
weights = [10, 20, 30, 30]
W = 60
memo = {}

def knapsack(i, c):
    if (i, c) in memo:
        return memo[(i, c)]
    if i == -1:
        return 0
    if c < weights[i]:
        memo[(i, c)] = knapsack2(i - 1, c)
        return memo[(i, c)]
    take = knapsack2(i - 1, c - weights[i]) + values[i]
    notake = knapsack2(i - 1, c)
    memo[(i, c)] = max(take, notake)
    return memo[(i, c)]

def knapsack2(i, c):
    if i == -1:
        return 0
    if c < weights[i]:
        return knapsack2(i - 1, c)
    take = knapsack2(i - 1, c - weights[i]) + values[i]
    notake = knapsack2(i - 1, c)
    return max(take, notake)

result = knapsack(len(values) - 1, 60)
print(f'knapset result: {result}')
result = knapsack(len(values) - 1, 50)
print(f'knapset result: {result}')
result = knapsack(len(values) - 1, 40)
print(f'knapset result: {result}')

