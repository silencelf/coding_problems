#! /usr/local/bin/python3
class Solution:
    def totalQueens(self, n):
        result = []
        cols, diag1, diag2 = set([]), set([]), set([])
        def helper(row, arr, n):
            for col in range(n):
                if col in cols:
                    continue
                if (row - col) in diag1:
                    continue
                if (row + col) in diag2:
                    continue
                if row == n - 1:
                    arr.append(col)
                    arr2 = arr.copy()
                    result.append(arr2)
                    arr.pop()
                else:
                    cols.add(col)
                    diag1.add(row - col)
                    diag2.add(row + col)
                    arr.append(col)
                    helper(row + 1, arr, n)
                    arr.pop()
                    cols.remove(col)
                    diag1.remove(row - col)
                    diag2.remove(row + col)

        helper(0, [], n)
        return result
    


n = 4
s = Solution()
result = s.totalQueens(n)
for arr in result:
    print(arr)

for arr in result:
    for i in range(n):
        for j in range(n):
            if j == arr[i]:
                print('Q', end= '')
            else:
                print('.', end = '')
        print('')
    print()
