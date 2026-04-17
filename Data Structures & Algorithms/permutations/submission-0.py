#
#
    #
#   Given an array nums of unique ints, return all possible permutations. 
#   
#   Notes:
#       - Any order
#
#           
#   Input: nums = [1,2,3]
#
#
#                   1            2          3 
#                2     3       1   3      2   1
#              3         2    3     1    1     2
#                        
#                                    
#
#
#
#
#
#   Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(currList):
            if len(currList) >= len(nums):
                res.append(currList.copy())
                return

            for i in range(len(nums)):
                if nums[i] in currList:
                    continue
                currList.append(nums[i])
                backtrack(currList)
                currList.remove(nums[i])
        backtrack([])
        return res


