class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        heap = [(-value, key) for key, value in dic.items()]
        heapq.heapify(heap)
        res = []
        for i in range(k):
            _, key = heapq.heappop(heap)
            res.append(key)
        return res