#!/usr/bin/python

class Solution:
    def addBinary(self, a, b):
        base = 2
        result = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0:
            current = 0
            if i >= 0:
                current += int(a[i])
            if j >= 0:
                current += int(b[j])
            current += carry
            result.append(current % base)
            carry = current // base
            i -= 1
            j -= 1
        if carry > 0:
            result.append(carry)
        print(list(reversed(result)))
        return list(reversed(result))


s = Solution()
print(s.addBinary('11', '1'))
