#! /usr/bin/python3
from timeit import timeit

def cacheit(cache):
    def inner(func):
        def cached(n):
            if n not in cache:
                ret = func(n)
                cache[n] = ret
            return cache[n]
        return cached
    return inner

def fib1(n):
    if n <= 2:
        return 1
    return fib1(n - 1) + fib1(n - 2)

@timeit
def raw_test():
    print(fib1(37))

#raw_test()

cache = {}
# recursion with memo
@cacheit(cache)
def fib2(n):
    if n <= 2:
        return 1
    return fib2(n - 1) + fib2(n - 2)

print(fib2(500))
print(cache)

#dp
def fib(n):
    dp = {1:1, 2:1}
    if n <= 2:
        return dp[n]
    for i in range(3, n + 1):
        r =  dp[i - 1] + dp[i - 2]
        dp[i] = r
    return dp[n]

#print(fib(10000))
