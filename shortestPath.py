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

result = shortest_path(adj, a)
print(result[0])
print(result[1])
