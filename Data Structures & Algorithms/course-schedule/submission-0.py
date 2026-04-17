class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {}
        for i in range(0, numCourses):
            adj[i] = []

        for p in prerequisites:
            print(p[1])
            adj[p[0]].append(p[1])
        
        visited = set()

        for i in range(0, numCourses):
            if not self.dfs(i, adj, visited):
                return False
        return True

    def dfs(self, src, adj, visited):

        if src in visited:
            return False
        
        visited.add(src)

        for neighbor in adj[src]:
            if not self.dfs(neighbor, adj, visited):
                return False
        
        visited.remove(src)
        return True
        