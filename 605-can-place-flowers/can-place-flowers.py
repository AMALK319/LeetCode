class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        
        m = len(flowerbed)
        i = 0

        while(i<m and n>0):
            if(flowerbed[i] == 1):
                i += 2
            else:
                if(i==m-1 or (i+1<m and flowerbed[i+1] == 0)):
                    flowerbed[i] = 1
                    n -= 1
                    i += 2
                else:
                    if i+3>=m : return False
                    i += 3

        if n == 0 : return True
        return False
        