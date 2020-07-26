#! /usr/bin/python

import time

def timeit(func):
    def timed(*args, **kw):
        ts = time.time()
        result = func(*args, **kw)
        te = time.time()
        print(f'time to execute {func.__name__}(): {(te - ts)} s')
        return result
    return timed
