class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        heap = []
        for i in range(len(points)):
            heapq.heappush(heap, (math.sqrt(((points[i][0]) ** 2) + ((points[i][1]) ** 2)), points[i]))
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result