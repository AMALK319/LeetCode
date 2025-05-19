class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)
        maxLocal = [[0]*(n-2) for _ in range(n-2)]

        print(maxLocal)

        for row in range(n-2):
            for col in range(n-2):
                maxGrid = 1
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        maxGrid = max(maxGrid, grid[i][j])
                maxLocal[row][col] = maxGrid
        return maxLocal
                

        