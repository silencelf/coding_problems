#! /usr/bin/python3

def fib1(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib1(10))
