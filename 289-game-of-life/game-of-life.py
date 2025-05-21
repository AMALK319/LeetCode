class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        state = [[0]*n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                    i = r - 1 if r>0 else 0
                    count = 0
                    while 0<=i<m and i<=r+1:
                        j = c - 1 if c>0 else 0
                        while 0<=j<n and j<=c+1:
                            if i == r and j == c :
                                j += 1
                            else:
                                if board[i][j] == 1:
                                    count += 1
                                j += 1
                        i += 1
                    if board[r][c] == 0 and count == 3:
                        state[r][c] = 1
                    elif board[r][c] == 1 and (count < 2 or count > 3):
                        state[r][c] = 0
                    elif board[r][c] == 1 and (count == 2 or count == 3):
                        state[r][c] = 1
                    else:
                        state[r][c] = board[r][c]
            
        for r in range(m):
            for c in range(n):
                board[r][c] = state[r][c]

        