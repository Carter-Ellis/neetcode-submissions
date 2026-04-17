class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        l, r = 0, 1

        while r < len(prices):
            dif = prices[r] - prices[l]
            if dif > 0:
                maxProfit = max(maxProfit, dif)
                r += 1
            else:
                l = r
                r += 1
                
        return maxProfit
                