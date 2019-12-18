from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        step, queue, visited = -1, deque([0]), set()
        numbers = [i*i for i in range(1, n + 1) if i*i <= n]

        while queue:
            l = len(queue)
            step += 1
            for _ in range(l):
                num = queue.popleft()
                if num == n:
                    return step
                if num in visited:
                    continue
                visited.add(num)
                for i in numbers:
                    queue.append(num + i)

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