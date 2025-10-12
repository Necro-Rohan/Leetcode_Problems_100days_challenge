class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def backtrack(row, cols, dig1, dig2, board):
            if row == n:
                res.append(["".join(r) for r in board])
                return 
            for col in range(n):
                if col in cols or (col-row) in dig1 or (col+row) in dig2:
                    continue
                
                board[row][col] = 'Q'
                cols.add(col)
                dig1.add(col-row)
                dig2.add(col+row)

                backtrack(row+1, cols, dig1, dig2, board)

                board[row][col] = '.'
                cols.remove(col)
                dig1.remove(col-row)
                dig2.remove(col+row)

        board = [['.' for _ in range (n)] for _ in range(n)]
        backtrack(0, set(), set(), set(), board)
        return res