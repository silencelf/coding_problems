class Solution:
    def numSquares(self, n: int) -> int:
        return -1


solution = Solution()
input = 12
expected = 3
result = solution.numSquares(input)
print(f'expected {expected}, actual result is {result}')

input = 13
expected = 2
result = solution.numSquares(input)
print(f'expected {expected}, actual result is {result}')

input = 9
expected = 1
result = solution.numSquares(input)
print(f'expected {expected}, actual result is {result}')