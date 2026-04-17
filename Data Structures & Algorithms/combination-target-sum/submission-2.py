class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        currList = []
        def rec(i, currSum):
            if currSum == target:
                result.append(currList.copy())
                return
            if i >= len(nums) or currSum > target:
                return
            currList.append(nums[i])
            rec(i, currSum + nums[i])
            if currList:
                currList.pop()
            rec(i + 1, currSum)
            return
        rec(0,0)
        return result