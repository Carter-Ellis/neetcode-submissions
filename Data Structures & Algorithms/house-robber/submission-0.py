class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0]
        for num in nums:
            temp = dp[1]
            dp[1] = max(dp[0] + num, dp[1])
            dp[0] = temp
        return dp[1]