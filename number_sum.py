"""
Given a list of numbers and a number k, return whether any two numbers from the
list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print("--- %.5f seconds ---" % (end - start))
        return ret
    return wrapper

def tests():
    input = [10, 15, 3, 7]
    k = 17
    result = check_sum(input, k)
    print('%d >> %s' % (k, result))
    result = check_sum2(input, k)
    print('%d >> %s' % (k, result))

    input = [0 for _ in range(0, 10000)]
    k = 10005
    result = check_sum(input, k)
    print('%d >> %s' % (k, result))
    result = check_sum2(input, k)
    print('%d >> %s' % (k, result))

@timer
def check_sum(input, k):
    for i in range(0, len(input)):
        for j in range(i + 1, len(input)):
            if input[i] + input[j] == k:
                return True
    return False

@timer
def check_sum2(input, k):
    cache = {}
    for i in input:
        if i in cache:
            return True
        else:
            cache[k - i] = i
    return False

# run tests
tests()
