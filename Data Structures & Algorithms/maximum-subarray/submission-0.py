class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currSub = 0
        for i in range(len(nums)):
            currSub = 0
            for j in range(i, len(nums)):
                currSub += nums[j]
                maxSum = max(maxSum, currSub)
                print(currSub)
        return maxSum
