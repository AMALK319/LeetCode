class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        pascals = []

        for i in range(numRows):
            if i == 0:
                pascals.append([1])
            elif i == 1:
                pascals.append([1,1])
            else:
                temp = [0]*(i+1)
                temp[0] = pascals[i-1][0]
                temp[i] = pascals[i-1][i-1]
                for j in range(1,i):
                    temp[j]=pascals[i-1][j-1]+pascals[i-1][j]
                pascals.append(temp)
        return pascals
                    
        