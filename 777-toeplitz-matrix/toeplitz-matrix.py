class Solution:
    """def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])

        for row in range(1,m):
            for col in range(1,n):
                if matrix[row][col] != matrix[row-1][col-1]:
                    return False
        return True """

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix:
            return True
        m, n = len(matrix), len(matrix[0])
        # Initially, store the first row except the last element
        prev_row = matrix[0][:-1]
        for i in range(1, m):
            current_row = matrix[i]
            # Compare prev_row with current_row starting from index 1
            for j in range(len(prev_row)):
                if prev_row[j] != current_row[j + 1]:
                    return False
            # Update prev_row to current_row except last element
            prev_row = current_row[:-1]
        return True    
            
        