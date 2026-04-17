class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
        
        for src, dest, weight in times:
            adj[src].append((weight, dest))

        shortest = {}
        minHeap = []
        heapq.heappush(minHeap, (0, k))

        while minHeap:
            weight1, node1 = heapq.heappop(minHeap)
            if node1 in shortest:
                continue
            
            shortest[node1] = weight1
            for weight2, node2 in adj[node1]:
                heapq.heappush(minHeap, (weight1 + weight2, node2))
        
        if len(shortest) != n:
            return -1
        
        time = 0
        for node, weight in shortest.items():
            time = max(weight, time)
        
        return time
            
