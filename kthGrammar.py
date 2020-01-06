class Solution:
    memo = { 0: [1, 0], 1: [0, 1] }
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        mod = int(k % 2)
        parent = -1
        if mod == 1:
            parent = self.kthGrammar(n - 1, int((k + 1)/2))
        else:
            parent = self.kthGrammar(n - 1, k/2)

        return self.memo[parent][mod]

s = Solution()
n,k = 1,1
r = s.kthGrammar(n, k)
print(r)
        
s = Solution()
n,k = 3,2
r = s.kthGrammar(n, k)
print(r)

s = Solution()
n,k = 4,5
r = s.kthGrammar(n, k)
print(r)