class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l, r = 0, len(nums) - 1
        
        nums.sort()
        ans = []

        for i in range(len(nums)):
            while l < r:
                if l <= i:
                    l += 1
                    continue
                if r <= i:
                    r -= 1
                    continue
                if nums[i] + nums[l] + nums[r] == 0 and [nums[i], nums[l], nums[r]] not in ans:
                    ans.append([nums[i], nums[l], nums[r]])
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
            l, r = 0, len(nums) - 1
        return ans
