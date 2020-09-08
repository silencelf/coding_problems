from collections import deque
class Solution:
    def openLock(self, deadends, target):
        visited, queue, step = set(deadends), deque(["0000"]), -1
        move = {str(i): [str((i+1)%10), str((i-1)%10)] for i in range(10)}

        while queue:
            step += 1
            for _ in range(len(queue)):
                item = queue.popleft()
                if item in visited:
                    continue
                if item == target:
                    return step
                visited.add(item)
                for i in range(4):
                    queue.append(item[:i] + move[item[i]][0] + item[i + 1:])
                    queue.append(item[:i] + move[item[i]][1] + item[i + 1:])
        return -1



solution = Solution()
deadends = [ "8888" ]
target = "0009"
expected = 1
result = solution.openLock(deadends, target)
print(f'expected {expected}, actual result is {result}')

deadends = [ "0201","0101","0102","1212","2002" ]
target = "0202"
expected = 6
result = solution.openLock(deadends, target)
print(f'expected {expected}, actual result is {result}')

deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"
expected = -1
result = solution.openLock(deadends, target)
print(f'expected {expected}, actual result is {result}')

deadends = ["0000"]
target = "8888"
expected = -1
result = solution.openLock(deadends, target)
print(f'expected {expected}, actual result is {result}')
