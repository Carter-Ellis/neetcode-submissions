class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}

        for num in nums:
            dic[num] = dic.get(num, 0) + 1
            if dic[num] > 1:
                return True
        return False

        