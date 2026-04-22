#
#
#   1. Make adjList and visited list
#   2. dfs on each node marking them as visited
#   3. If node is not visited we add 1 to count
#

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0

        adjList = {i : [] for i in range(n)}

        visited = set()

        for e1, e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)
        
        def dfs(curr):
            if curr in visited:
                return
            visited.add(curr)
            for node in adjList[curr]:
                dfs(node)
        
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count