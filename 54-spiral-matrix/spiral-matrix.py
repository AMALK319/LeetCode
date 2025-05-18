class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
    

        def getRow(i, s, e):
            return matrix[i][s:e]
        def getCol(j, s, e):
            return [matrix[i][j] for i in range(s,e)]

        r = c = 0
        while(r<=m//2 and c<=n//2 and len(res)<n*m):
                res += getRow(r,c,n-c)
                res += getCol(n-1-c, r+1,m-r-1)
                if r!= m-1-r :
                    res += getRow(m-1-r,c,n-c)[::-1]
                if c != n-1-c:
                    res += getCol(c, r+1,m-r-1)[::-1]
                r += 1
                c += 1
        return res

                


       

        