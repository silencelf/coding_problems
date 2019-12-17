class Solution:
    def openLock(self, deadends, target):
        return 0



solution = Solution()
deadends = [ "8888" ]
target = "0009"
expected = 1
result = solution.openLock(deadends, target)
print('expected 1, actual result is' + result)