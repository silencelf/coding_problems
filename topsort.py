#! /usr/bin/python3

class Vertex:
    value = ''
    neighbors = []
    def __init__(self, value, neighbors):
        self.value = value
        self.neighbors = neighbors
    def __str__(self):
        return self.value

def topsort(vertexes):
    visited = set({})
    result = []
    index = len(vertexes) - 1
    for v in vertexes:
        if v not in visited:
            dfs(v, index, visited, result)
    return result

def dfs(v, index, visited, result):
    visited.add(v)
    for n in v.neighbors:
        if n not in visited:
            index = dfs(n, index, visited, result)
            print(index)
    result.append(v)
    return index - 1

v1 = Vertex('F', [])
v2 = Vertex('E', [v1])
v3 = Vertex('D', [v1])
v4 = Vertex('C', [v2])
v5 = Vertex('B', [v3])
v6 = Vertex('A', [v4, v5])

input = [v1, v2, v3, v4 ,v5, v6]
ret = topsort(input)
for v in ret:
    print(v)
