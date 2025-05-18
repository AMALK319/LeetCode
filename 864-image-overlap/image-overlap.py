class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        def translate(x_shift, y_shift):
            num = 0
            for r in range(n):
                for c in range(n):
                    if (0<=r+x_shift<n and 0<=c+y_shift<n and img1[r+x_shift][c+y_shift] == 1 and img2[r][c] == 1):
                        num += 1
            return num

        
        return max([translate(x,y) for x in range(-n,n) for y in range(-n,n)])


        