class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = []

        for i in range(1, len(points)):
            heapq.heappush(minHeap, (abs(points[0][0] - points[i][0]) + abs(points[0][1] - points[i][1]), tuple(points[0]), tuple(points[i])))
        
        visited = set()
        visited.add(tuple(points[0]))
        minCost = 0

        while minHeap:
            cost, src, node = heapq.heappop(minHeap)
            if tuple(node) in visited:
                continue

            minCost += cost
            visited.add(tuple(node))

            for point in points:
                if tuple(point) not in visited:
                    heapq.heappush(minHeap, (abs(node[0] - point[0]) + abs(node[1] - point[1]), tuple(node), tuple(point)))

        return minCost