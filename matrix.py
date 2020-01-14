#! /local/bin/python3

from collections import deque

def distance(matrix):
    if not matrix:
        return []
    rl, cl = len(matrix), len(matrix[0])
    for sr in range(rl):
        for sc in range(cl):
            visited = set([])
            queue, dept, found = deque([(sr, sc)]), -1, False
            while queue and not found:
                dept += 1
                q2 = deque([])
                for (x, y) in queue:
                    if (x, y) in visited:
                        continue
                    visited.add((x, y))
                    if matrix[x][y] == 0:
                        matrix[sr][sc] = dept
                        found = True
                        break
                    if x > 0:
                        q2.append((x - 1, y))
                    if x < rl - 1:
                        q2.append((x + 1, y))
                    if y > 0:
                        q2.append((x, y - 1))
                    if y < cl - 1:
                        q2.append((x, y + 1))
                queue = q2
    return matrix

matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
# distance(matrix)
print(matrix)

matrix = [[0, 0,0], [0, 1, 0], [1, 1, 1]]
# distance(matrix)
print(matrix)

matrix = [[0, 1, 0],[0, 1, 0],[0, 1, 0],[0, 1, 0],[0, 1, 0]]
distance(matrix)
print(matrix)
