class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations, currComb = [], []
        currSum = 0
        def rec(i, currSum):
            if i >= len(nums) or currSum > target:
                return

            if currSum == target:
                combinations.append(currComb.copy())
                return
            

            currComb.append(nums[i])
            currSum += nums[i]
            rec(i, currSum)
            currComb.pop()
            currSum -= nums[i]
            rec(i + 1, currSum)
        rec(0, currSum)
        return combinations