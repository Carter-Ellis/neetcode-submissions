#
#
#   Given an array of ints (candidates) and a target int (target), return a list of all unique combinations of condidates
#   where the chosen numbers sum to target.
#
#   Notes:
#       - candidates may contain duplicates
#       - Each element can be chosen at most once with a combination.
#       - No duplicate combinations
#       - May return combos in any order.
#       - Ints in the combos may be any order
#
#
#   Input: candidates = [9,2,2,4,6,1,5], target = 8
#   
#
#   Output: [
#     [1,2,5],
#     [2,2,4],
#     [2,6]
#   ]
#                   
#                   
#            
#
#
#
#
#   
#
#


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def rec(currList, currSum, index):
            
            if currSum == target:

                newList = currList.copy()
                newList.sort()
                print(res)
                if newList not in res:
                    res.append(newList.copy())
                return

            if index >= len(candidates):
                return
            
            

            currSum += candidates[index]
            currList.append(candidates[index])

            rec(currList, currSum, index + 1)

            currSum -= candidates[index]
            currList.remove(candidates[index])

            rec(currList, currSum, index + 1)
        rec([], 0, 0)
        return res



















