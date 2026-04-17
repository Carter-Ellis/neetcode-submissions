class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        
        maxHeap = []
        for num, count in dic.items():
            maxHeap.append((-count, num))
        heapq.heapify(maxHeap)

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(maxHeap)[1])
        return ans