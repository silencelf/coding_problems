class Solution:
    def findMinHeightTrees(self, n: int, edges):
        # create adjacent array
        adj = [set() for _ in range(n)]
        for (u,v) in edges: 
            adj[u].add(v)
            adj[v].add(u)

        leaves = [i for i in range(n) if len(adj[i])==1]
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1:
                    newLeaves.append(j)
            leaves = newLeaves
        return leaves


s = Solution()
n, edges = 4, [[1, 0], [1, 2], [1, 3]]
graph = [set() for _ in range(n)]
for (u,v) in edges: 
    graph[u].add(v)
    graph[v].add(u)
print(graph)
r = s.findMinHeightTrees(n,edges)
print(r)

n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
r = s.findMinHeightTrees(n, edges)
print(r)
