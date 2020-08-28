#! /bin/python
"""
move a robot from (1, 1) to (M, N), the robot can only move right or move up.
how many distinct path are there for the rebot to move to destination?
"""
from collections import deque

def dp(m, n):
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 1 or n == 1:
        memo[(m, n)] = 1
        return 1
    result = dp(m, n - 1) + dp(m - 1, n)
    memo[(m, n)] = result
    return result

# this is slow
def dp2(M, N):
    V = { (1,1): 1 }
    for m in range(1, M + 1):
        V[(m, 0)] = 0
    for n in range(1, N + 1):
        V[(0, n)] = 0
    q = deque([(1,1)])
    while q:
        print(q)
        (m, n) = q.popleft()
        if (m, n) not in V:
            V[(m, n)] = V[(m-1, n)] + V[(m, n-1)]
        if m + 1 <= M:
            q.append((m+1, n))
        if n + 1 <= N:
            q.append((m, n+1))
    return V[(M,N)]

def dp3(M, N):
    if M < N:
        dp3(N, M)
    V = { (1,1): 1 }
    for m in range(1, M + N):
        V[(m, 0)] = 0
        V[(0, m)] = 0
    q = deque([(1,1)])
    for m in range(3, M + N + 1):
        for n in range(1, m):
            V[(n, m - n)] = V[(n-1, m - n)] + V[(n, m-n-1)]
    return V[(M,N)]

cases = [(5,5), (5,6), (6,5), (6,6), (2,7), (3,6), (3,7), (1000, 1000)]
for (m, n) in cases:
    memo = {}
    result = dp3(m, n)
    print(f'dp3({m}, {n}) = {result}')
    result = dp(m, n)
    print(f'dp({m}, {n}) = {result}')
