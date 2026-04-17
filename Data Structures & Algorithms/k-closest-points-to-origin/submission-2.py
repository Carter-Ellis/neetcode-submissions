#
#
#
#   Input: points[i] = [xi, yi], k (int)
#   
#   Output: k closest points to the origin.
#
#   Notes:
#       - Euclidean distance = sqrt((x1 - x2)^2 + (y1 - y2)^2))
#       - Any order
#
#   for each point:
#       -> Calculate distance
#       -> Insert into minHeap
#   -> pop heap k times and return result
#
#
#   Data Structure: MinHeap
#

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for p in points:
            distance = math.sqrt(p[0]**2 + p[1]**2)
            heapq.heappush(minHeap, (distance, p[0], p[1]))
        for i in range(k):
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
        return res