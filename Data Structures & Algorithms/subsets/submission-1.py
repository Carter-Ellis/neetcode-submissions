'''
    [1,2,3,4,5]
     1 2 3 4 5 currIndex + 1 + i, i = 0
     1 3 4 5

     
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, currSet = [], []
        
        
        def backtrack(i, subsets, currSet): 
            
            if i >= len(nums):
                subsets.append(currSet.copy())
                return

            currSet.append(nums[i])
            backtrack(i + 1, subsets, currSet)
            currSet.pop()

            backtrack(i + 1, subsets, currSet)

        backtrack(0, subsets, currSet)
        return subsets


        
        