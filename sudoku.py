class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        cols, rows = [], []
        for _ in range(9):
            rows.append(set([]))
            cols.append(set([]))
        squares = []
        for _ in range(3):
            squares.append([set([]),set([]),set([])])
        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == '.':
                    continue
                rows[row].add(value)
                cols[col].add(value)
                squares[int(row/3)][int(col/3)].add(value)
        def nextIndex(r, c):
            if c < 8:
                return (r, c+1)
            elif r < 8:
                return (r+1, 0)
            else:
                return None
        def helper(row, col):
            if row > 8 or col > 8:
                return False
            srow, scol  = int(row/3), int(col/3)
            if board[row][col] == '.':
                for inumber in range(1, 10):
                    i = str(inumber)
                    if i in rows[row]:
                        continue
                    if i in cols[col]:
                        continue
                    if i in squares[srow][scol]:
                        continue
                    if row == 8 and col == 8:
                        board[row][col] = i
                        print(board)
                        return True
                    else:
                        board[row][col] = i
                        print(board)
                        rows[row].add(i)
                        cols[col].add(i)
                        squares[srow][scol].add(i)
                        (nr,nc) = nextIndex(row, col)
                        success = helper(nr, nc)
                        if success:
                            return True
                        else:
                            rows[row].remove(i)
                            cols[col].remove(i)
                            squares[srow][scol].remove(i)
                            board[row][col] = '.'
            else:
                if row == 8 and col == 8:
                    return True
                (nr,nc) = nextIndex(row, col)
                helper(nr, nc)
            return False
                
        helper(0, 0)
                            
s = Solution()
input = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(input)
print(input)