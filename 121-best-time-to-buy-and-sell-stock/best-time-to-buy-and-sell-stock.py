class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyingPrice = prices[0]
        for i in range(1,len(prices)):
            if prices[i]<buyingPrice:
                buyingPrice = prices[i]
            else: 
                maxProfit = max(maxProfit, prices[i]-buyingPrice)
        return maxProfit
        