class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        startPrice = prices[0]

        for i in range(1, len(prices)):
            profit = prices[i] - startPrice
            maxProfit = max(profit, maxProfit)
            if startPrice > prices[i]:
                startPrice = prices[i]

        return maxProfit
