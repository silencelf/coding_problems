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
    # have to write a priority queue myself
    arr = [(0, s)] + [(math.inf, v) for v in adj if v != s]
    D = { v: math.inf for v in adj }
    D[s] = 0
    print(D)
    P = { v: None for v in adj }
    print(P)
    heap = Heap(arr)

    while True:
        v = heap.extract()
        print(v)
        print('heap:')
        print(heap)
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
