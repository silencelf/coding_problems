#! /usr/bin/python

import math
from heap import Heap

a = 'A' 
b = 'B' 
c = 'C' 
d = 'D' 
e = 'E' 
f = 'F' 

# initialize
adj = {}
adj[a] = [(4, b), (2 ,c)]
adj[b] = [(5 ,c), (10 ,d)]
adj[c] = [(3 ,e)]
adj[d] = [(11 ,f)]
adj[e] = [(4 ,d)]
adj[f] = []

def shortest_path(adj, s):
    arr, D, P = [], {}, {}
    for v in adj:
        P[v] = None
        if v == s:
            arr.append((0, v))
            D[v] = 0
        else:
            arr.append((math.inf, v))
            D[v] = math.inf
    heap = Heap(arr)

    while True:
        v = heap.extract()
        if v is None:
            break
        current = v[1]
        for pair in adj[current]:
            w, e = pair 
            nw = D[current] + w
            if nw < D[e]:
                D[e] = nw
                P[e] = current
                heap.decrease(D[e], e)
    return (D, P)

# result = shortest_path(adj, a)
# print(result[0])
# print(result[1])

parent = {}
for v in adj:
    for e in adj[v]:
        d, v2 = e
        if v2 not in parent:
            parent[v2] = [(d, v)]
        else:
            parent[v2].append((d, v))
parent[a] = [(0, a)]

memo = {}
def sp(adj, s, v, D, P):
    if (s, v) in memo:
        return memo[(s, v)]
    if s == v:
        return 0
    for (w, i) in adj[v]:
        d = sp(adj, s, i, D, P) + w
        # d(s, v)  = min(d(s, u) + d(u, v) for u belongs to {incomming edges of v})
        if d < D[v]:
            D[v] = d
            P[v] = i
    # memo actually adds items by the topological order of G(v, e)
    memo[(s, v)] = D[v]
    print(f'memo extends to: {memo}')
    return D[v]

def shortest_path_dp(adj, s):
    D = { v: math.inf for v in adj}
    D[s] = 0
    P = {}
    for v in parent:
        sp(adj, s, v, D, P)
    return (D, P)

result = shortest_path_dp(parent, a)
print(result)