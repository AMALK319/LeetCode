class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        state = [[0]*n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                state[r][c] = matrix[r][c]
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] != 0:
                    continue
                else:
                    for i in range(m):
                        state[i][c] = 0
                    for i in range(n):
                        state[r][i] = 0

        for r in range(m):
            for c in range(n):
                matrix[r][c] = state[r][c]
                    