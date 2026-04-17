class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        res = 0
        for i in range(1, len(nums) + 1):
            total += i
        for i in range(len(nums)):
            res += nums[i]
        return total - res
