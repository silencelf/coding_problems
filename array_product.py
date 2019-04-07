"""
Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the original array except
the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be
[2, 3, 6].

Follow-up: what if you can't use division?
"""

# brute force solution
# time complexity is O(n*n)
def array_product(input):
    result = []
    for i in range(len(input)):
        product = 1
        for j in range(len(input)):
            if i != j:
                product *= input[j]
        result.append(product)

    print(result)
    return result

# use division, but if one of the element is 0 then everythin falls aport
# time complexity is O(n)
def array_product_division(input):
    product = 1
    for i in input:
        product *= i

    return [product/i for i in input]

input = [1, 2, 3, 4, 5]
ret = array_product(input)
print('result is : %a' % ret)
ret = array_product_division(input)
print('result is : %a' % ret)
print('result should be : %a' % [120, 60, 40, 30, 24])
