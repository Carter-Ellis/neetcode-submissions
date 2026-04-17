class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = False
        def rec(index):
            if index > len(nums) - 1:
                return False
            if index == len(nums) - 1:
                return True
            for i in range(nums[index]):   
                if rec(index + i + 1):
                    return True
            return False  
        return rec(0)