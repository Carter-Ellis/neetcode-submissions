class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        minHeap = nums
        heapq.heapify(minHeap)

        ans = 1
        currNum = 0
        prevNum = heapq.heappop(minHeap)
        count = 1
        while minHeap:
            
            currNum = heapq.heappop(minHeap)
            
            if currNum == prevNum + 1:
                count += 1
                ans = max(count, ans)
            elif currNum != prevNum:
                count = 1
            prevNum = currNum
        return ans
