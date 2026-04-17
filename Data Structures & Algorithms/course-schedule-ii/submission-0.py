class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(0, numCourses):
            adj[i] = []
        
        for p in prerequisites:
            adj[p[0]].append(p[1])
        
        topSort = []

        visited = set()
        path = set()

        for i in range(0, numCourses):
            if not self.dfs(i, visited, path, adj, topSort):
                return []

        return topSort

    def dfs(self, src, visited, path, adj, topSort):
        
        if src in path:
            return False
        
        if src in visited:
            return True

        visited.add(src)
        path.add(src)



        for neighbor in adj[src]:
            if not self.dfs(neighbor, visited, path, adj, topSort):
                return False

        topSort.append(src)
        path.remove(src)
        return True