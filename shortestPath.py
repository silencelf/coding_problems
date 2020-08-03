import math
from vertex import Vertex
from queue import PriorityQueue

a = Vertex('A') 
b = Vertex('B') 
c = Vertex('C') 
d = Vertex('D') 
e = Vertex('E') 
f = Vertex('F') 

adj = {}
adj[a] = [(b, 4), (c, 2)]
adj[b] = [(c, 5), (d, 10)]
adj[c] = [(e, 3)]
adj[d] = [(f, 11)]
adj[e] = [(d, 4)]
adj[f] = []

def shortest_path(adj, s):
    # have to write a priority queue myself
    q = PriorityQueue()
    for v in adj:
        if v == s:
            q.put(0, v)
        else:
            q.put(math.inf, v)
    print(q)

shortest_path(adj, a)
