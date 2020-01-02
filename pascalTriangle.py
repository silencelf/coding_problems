def generate(numRows):
    memo = {}
    def compute(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if j == 0 or i == j:
            return 1
        a = compute(i-1, j-1)
        b = compute(i-1, j)
        memo[(i,j)] = a + b
        return a + b
    result = []
    for i in range(numRows):
        result.append([])
        for j in range(i + 1):
            result[i].append(compute(i, j))
    return result

tri = generate(5)
print(tri)
tri = generate(25)
print(tri)
