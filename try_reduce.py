#!/bin/python3

import functools

def my_add(a, b):
    result = a + b
    print(f'{a} + {b} = {result}')
    return result

r = functools.reduce(my_add, range(10))
