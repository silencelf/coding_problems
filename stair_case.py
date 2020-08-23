"""
There's a staircase with N steps, and you can climb 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb
the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2
    What if, instead of being able to climb 1 or 2 steps at a time, you could
    climb any number from a set of positive integers X? For example, if X = {1,
            3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your
    function to take in X.
"""
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print("--- %s seconds ---" % (end - start))
        return ret
    return wrapper

def test_staircase():
    suits = [1, 2, 3, 4 ,5 , 11, 30]
    for i in suits:
        print(staircase(i))
        print(staircase_iter(i))
        print(staircase_multi(i, [1, 2]))

def staircase_iter(n):
    a, b = 1, 2
    for _ in range(1, n):
        a, b = b, a + b
    return a

def staircase(n):
    if n <= 1:
        return 1
    else:
        return staircase(n - 1) + staircase(n - 2)

def staircase_dp(n, dict):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in dict:
        return dict[n]
    ret = staircase_dp(n - 1, dict) + staircase_dp(n - 2, dict)
    dict[n] = ret
    return ret

def staircase_multi(n, X):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return sum(staircase_multi(n - x, X) for x in X if n - x >= 0)

# usally i would stop with this as it is readable and it is fast
def staircase_multi_dp(n, X, cache):
    if n < 0:
        return 0
    if n == 0:
        return 1

    if n in cache:
        return cache[n]

    cache[n] = sum(staircase_multi_dp(n - x, X, cache) for x in X if n - x >= 0)
    print(f'cached updated: {cache}');
    return cache[n]

# but for pactice let's try the iterative way
def staircase_multi_iter(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if n - x >= 0)

    return cache[n]

# this is where the tests begin
count = 35
steps = [2, 3]

# readablily and performance
start = time.time()
print(staircase_multi(count, steps))
end = time.time()
print("flexible: --- %.4f seconds ---" % (end - start))

# readablily and performance
start = time.time()
print(staircase_multi_dp(count, steps, {}))
end = time.time()
print("flexible: --- %.4f seconds ---" % (end - start))

# 
# # brutal force
# start = time.time()
# print(staircase(count))
# end = time.time()
# print("simple: --- %.4f seconds ---" % (end - start))
# 
# # dynamic programming
# start = time.time()
# dict = {}
# print(staircase_dp(count, dict))
# end = time.time()
# print(dict)
# print("simple DP: --- %.4f seconds ---" % (end - start))
# 
# # iterative
# start = time.time()
# print(staircase_iter(count))
# end = time.time()
# print("simple iterator: --- %.4f seconds ---" % (end - start))
# 
# # flexable but not efficient
# start = time.time()
# print(staircase_multi(count, steps))
# end = time.time()
# print("flexible: --- %.4f seconds ---" % (end - start))
# 
# # flexable but not efficient
# start = time.time()
# cache = {}
# print(staircase_multi_dp(count, steps, cache))
# end = time.time()
# print(cache)
# print("flexible DP: --- %.4f seconds ---" % (end - start))
# 
# # flexable iteritave with dp
# start = time.time()
# print(staircase_multi_iter(count, steps))
# end = time.time()
# print("flexible iter DP: --- %.4f seconds ---" % (end - start))
# 
# #test_staircase()
# 