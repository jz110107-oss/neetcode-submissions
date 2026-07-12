class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0

        for i in range(len(prices)):
            if prices[i] - minprice > 0:
                maxprofit = max(maxprofit, prices[i] - minprice)
            minprice = min(minprice, prices[i])
        
        return maxprofit
        