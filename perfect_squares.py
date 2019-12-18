from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        step, queue, visited, nq = -1, [0], set(), []
        numbers = [i**2 for i in range(1, int(n**0.5) + 1)]

        while queue:
            step += 1
            for num in queue:
                if num == n:
                    return step
                if num in visited:
                    continue
                visited.add(num)
                for i in numbers:
                    newVal = num + i
                    if newVal > n:
                        break;
                    nq.append(newVal)
            queue, nq = nq, []
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

input = 1
expected = 1
result = solution.numSquares(input)
print(f'expected {expected}, actual result is {result}')