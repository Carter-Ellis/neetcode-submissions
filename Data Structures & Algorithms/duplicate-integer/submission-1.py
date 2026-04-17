class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = {}
        for num in nums:
            if num not in values:
                values[num] = 0
            values[num] += 1
            if values[num] > 1:
                return True
        return False