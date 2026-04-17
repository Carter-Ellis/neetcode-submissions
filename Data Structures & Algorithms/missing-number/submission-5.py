class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        target = 0
        total = 0
        for i in range(len(nums) + 1):
            target += i
            if i < len(nums):
                total += nums[i]

        if target == total:
            return 0
        else:
            return target - total 
        