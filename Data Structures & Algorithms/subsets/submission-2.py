
#
#   Given an array of nums, return all possible subsets of num
#   
#   Notes:
#       - Cannot contain duplicate subsets
#       - May return solution in any order
#       - Unique numbers
#       - Not ordered
#
#   index = 2
#   subList = [2,3]
#
#   Input: nums = [1,2,3]
#                  i 
#   Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
#
#

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def rec(subList: List[int], index: int) -> None:
            nonlocal res
            if index >= len(nums):
                return

            for i in range(index,len(nums)):
                subList.append(nums[i])
                res.append(subList.copy())
                rec(subList, i + 1)
                subList.pop()

        rec([], 0)
        return res