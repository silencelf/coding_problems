def try_reduce(nums):
    return reduce(lambda x, y: x + y, nums)
nums = [i for i in range(10)
result = try_reduce(nums)
print(result)

