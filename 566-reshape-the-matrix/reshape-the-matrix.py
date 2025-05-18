class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        m, n = len(mat), len(mat[0])
        reshaped = [[0]*c for _ in range(r)]

        if r*c != m*n: return mat

        i = j = 0
        for row in range(r):
            for col in range(c):
                if j == n:
                    j = 0
                    i += 1
                reshaped[row][col] = mat[i][j]
                j += 1
        
        return reshaped

        