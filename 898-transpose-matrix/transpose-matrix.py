class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        N , M = len(matrix), len(matrix[0])
        transpose = [[0]* N for _ in range(M)]

        for row in range(M):
            for col in range(N):
                transpose[row][col] = matrix[col][row]

        return transpose 