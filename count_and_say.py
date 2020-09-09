#!/bin/python

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        num = self.countAndSay(n - 1)
        last, count = num[0], 1
        cs = ""
        for i in num[1:]:
            if last != i:
                cs += str(count) + last
                last = i
                count = 1
            else:
                count += 1
        cs += str(count) + last
        return cs

sol = Solution()
print(sol.countAndSay(2))
print(sol.countAndSay(3))
print(sol.countAndSay(4))
print(sol.countAndSay(5))
print(sol.countAndSay(6))
print(sol.countAndSay(7))
print(sol.countAndSay(8))
print(sol.countAndSay(9))
print(sol.countAndSay(10))
