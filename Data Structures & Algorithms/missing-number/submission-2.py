class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        res = 0
        for i in range(len(nums)):
            total += i
            res += nums[i]
        total += len(nums)
        return total - res
