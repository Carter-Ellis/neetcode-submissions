class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        i = 0
        while i < k:
            num = heapq.heappop(nums)
            if i == k - 1:
                return -num
            i += 1
        return 0 
            
