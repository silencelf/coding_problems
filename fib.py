#! /usr/bin/python3

import time

def timeit(func):
    def timed(*args, **kw):
        ts = time.time()
        result = func(*args, **kw)
        te = time.time()
        print('%2.2fms' % (te - ts))
        return result
    return timed

def fib1(n):
    if n <= 2:
        return 1
    return fib1(n - 1) + fib1(n - 2)

#print(fib1(10))

# recursion with memo
# TODO: wirte a decorator function to momorize the value
dp = {}
def fib2(n):
    r = 0
    if n in dp:
        return dp[n]
    if n <= 2:
        r = 1
        dp[n] = r
        return r
    r =  fib2(n - 1) + fib2(n - 2)
    dp[n] = r
    return r

#print(fib2(1000))

#dp
def fib(n):
    dp = {1:1, 2:1}
    if n <= 2:
        return dp[n]
    for i in range(3, n + 1):
        r =  dp[i - 1] + dp[i - 2]
        dp[i] = r
    return dp[n]

print(fib(10000))
