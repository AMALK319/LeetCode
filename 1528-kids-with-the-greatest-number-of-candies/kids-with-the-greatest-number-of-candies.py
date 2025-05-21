class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n, result = len(candies), []
        maxCandies = max(candies)
        for candie in candies:
            if candie+extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        return result
        