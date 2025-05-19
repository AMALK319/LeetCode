class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in board[row][col+1:]:
                    return False
                for i in range(row+1,9):
                    if board[row][col] == board[i][col]:
                        return False
                boxRow = 3 * (row // 3)
                boxCol = 3 * (col // 3)
                for i in range(boxRow,boxRow+3):
                    for j in range(boxCol,boxCol+3):
                        if (i != row and j != col) and board[row][col] == board[i][j]:
                            return False
        return True

    """ Neetcode Solution: 
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if(board[r][c] in rows[r] or
                   board[r][c] in cols[c] or
                   board[r][c] in squares[(r//3, c//3)]):
                   return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True """ 
    