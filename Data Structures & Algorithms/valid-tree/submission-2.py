#
# Valid Tree: 
#       - No cycles
#       - Can't be separated
#
#
#

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i : [] for i in range(n)}

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        visited = set()

        def dfs(curr) -> bool:
            # Found a cycle
            if curr in visited:
                return False

            visited.add(curr)

            for node in adjList[curr]:
                adjList[node].remove(curr)
                if not dfs(node):
                    # Found cycle
                    return False
            
            
            return True
        

        if not dfs(0):
            return False
            
        if len(visited) != n:
            return False

        return True