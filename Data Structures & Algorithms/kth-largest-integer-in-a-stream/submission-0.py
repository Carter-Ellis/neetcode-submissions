class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify_max(self.nums)
        

    def add(self, val: int) -> int:
        
        heapq.heappush_max(self.nums, val)
        temp = self.nums.copy()
        res = 0
        for i in range(self.k):
            res = heapq.heappop_max(temp)
        return res
        
