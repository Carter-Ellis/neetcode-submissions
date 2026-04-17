class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        count = (n * (n + 1)) // 2 
        for i in range(len(nums)):
            count -= nums[i]

        return count
