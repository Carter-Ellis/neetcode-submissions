class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            dic[target - nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in dic and i != dic[nums[i]]:
                return [i,dic[nums[i]]]
        return [] 