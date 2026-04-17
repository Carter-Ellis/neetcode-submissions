#
#
#   Given an array of distinct ints (nums) and a target int (target), return a list of unique combinations of nums where the
#   chosen numbers sum to target.
#
#   Notes:
#       - The same nums maybe chosen multiple times
#       - Combinations are the same if the frequency of the chosen number is the same, otherwise they are different.
#       - Return any order
#       - Combinations can be in any order
#
#   global vars:
#       res = []    
#   func vars:
#       currSum = 0
#       currCombo = []
#       index = 0
#
#   Input:
#   nums = [2,5,6,9]
#   target = 9
#
#   Output: [[2,2,5],[9]]
#
#

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def rec(currCombo : List[int], currSum: int, index: int) -> None:
            
            currSum += nums[index]
            
            currCombo.append(nums[index])
            if currSum > target:
                currCombo.remove(nums[index])
                return
            if currSum == target:
                currCombo.sort()
                newCombo = currCombo.copy()
                if newCombo not in res:
                    res.append(newCombo)
                currCombo.remove(nums[index])
                return

            for i in range(len(nums)):
                rec(currCombo, currSum, i)
            currCombo.remove(nums[index])
        for i in range(len(nums)):
            rec([], 0, i)
        return res










