class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        res = [False] * len(candies)
        maxCandies = 0
        for candie in candies:
            maxCandies = max(maxCandies, candie)
        for i in range(len(candies)):
            if candies[i]+extraCandies >= maxCandies:
                res[i] = True
        return res
        
    
        