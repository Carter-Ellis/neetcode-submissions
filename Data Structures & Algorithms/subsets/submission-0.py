'''
    [1,2,3,4,5]
     1 2 3 4 5 currIndex + 1 + i, i = 0
     1 3 4 5

     
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def rec(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            rec(i + 1)

            subset.pop()
            rec(i + 1)
        rec(0)
        return res


        
        