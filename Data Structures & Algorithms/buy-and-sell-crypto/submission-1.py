class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        startDay = prices[0]
        maxProf = 0
        for i in range(1, len(prices)):
            maxProf = max(maxProf, prices[i] - startDay)
            if startDay > prices[i]:
                startDay = prices[i]
        return maxProf