class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i in range(len(nums)):
            diffs[target - nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in diffs and i != diffs[nums[i]]:
                return [min(i,diffs[nums[i]]), max(i,diffs[nums[i]])]