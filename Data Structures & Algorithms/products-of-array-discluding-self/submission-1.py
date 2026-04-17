class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prefix = []
        postfix = []
        product = 1
        for num in nums:
            product *= num
            prefix.append(product)
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            product *= nums[i]
            postfix.insert(0, product)
            
        for i in range(len(nums)):
            left = 1
            right = 1
            if i - 1 > -1:
                left = prefix[i - 1]
            if i + 1 < len(nums):
                right = postfix[i + 1]
            ans.append(left * right)
        return ans