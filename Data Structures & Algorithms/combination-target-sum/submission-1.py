class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        currList = []
        def rec(index, currSum):
            sorted_currList = sorted(currList)
            if currSum == target and not any(sorted(sublist) == sorted_currList for sublist in result):
                result.append(currList.copy())
                currList.pop()
                return
            if index >= len(nums) or currSum > target:
                currList.pop()
                return
            for i in range(len(nums)):
                currList.append(nums[i])
                rec(i, currSum + nums[i])
            if currList:
                currList.pop()
            return
        rec(0,0)
        return result