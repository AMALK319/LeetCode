class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        l, r = 0, n-1
        t, b = 0, n-1

        e = 0
        while(l<=r):
           
            for col in range(l,r+1):
                e += 1
                res[t][col] = e
            t += 1

            for row in range(t,b+1):
                e += 1
                res[row][r] = e
            r -= 1

            if(t>b or l>r):
                break

            for col in range(r, l-1, -1):
                e += 1
                res[b][col] = e
            b -= 1

            for row in range(b,t-1, -1):
                e += 1
                res[row][l] = e
            l += 1
            
        return res
