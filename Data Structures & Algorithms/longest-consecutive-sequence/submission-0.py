class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            numSet.add(num)

        heap = list(numSet)
        heapq.heapify(heap)

        prevNum = 0
        count = 0
        maxCount = 0
        for i in range(len(heap)):
            num = heapq.heappop(heap)
            if num == prevNum + 1:
                count += 1
            else:
                count = 1
            prevNum = num
            maxCount = max(maxCount, count)
        return maxCount