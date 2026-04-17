class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + ((r - l) // 2)

            if nums[r] < nums[l]:
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    while l + 1 < r and nums[l] < nums[l + 1]:
                        l += 1
                    l += 1
            elif nums[l] < nums[r]:
                r = mid - 1

        return nums[l]