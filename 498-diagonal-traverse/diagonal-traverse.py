class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        diagonals = []
        
        row = col = 0
        go_up = True
        while len(diagonals) != m * n:
            if go_up:
                while row >= 0 and col < n:
                    diagonals.append(mat[row][col])
                    row -= 1
                    col += 1
                if col == n:
                    col -= 1
                    row += 2
                else:
                    row += 1
                go_up = False
            else:
                while col >= 0 and row < m:
                    diagonals.append(mat[row][col])
                    col -= 1
                    row += 1
                if row == m:  
                    row -= 1
                    col += 2
                else:
                    col += 1
                go_up = True
        return diagonals