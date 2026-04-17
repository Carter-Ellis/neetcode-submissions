#
#
#   Given an array of ints (nums), return all possible subsets.
#
#   Notes:
#       - nums may contain duplicates
#       - solution must NOT contain duplicate subsets.
#       - solution can be any order
#
#
#   Global vars:
#       - res = [[]]
# 
#   rec vars:
#       - subList = []
#       - index = 0


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        def rec(subList, index) -> None:
            if index >= len(nums):
                return
            subList.append(nums[index])
            if subList not in res:
                res.append(subList.copy())
            rec(subList, index + 1)
            subList.remove(nums[index])
            rec(subList, index + 1)
        rec([], 0)
        return res