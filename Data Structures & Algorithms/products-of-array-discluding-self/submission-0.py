class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            product = 0
            for j in range(len(nums)):
                if j == 0 and j != i:
                    product = nums[j]
                elif j == 0 and j == i:   
                    product = 1
                elif j != i:
                    product *= nums[j]
            ans.append(product)
        return ans
