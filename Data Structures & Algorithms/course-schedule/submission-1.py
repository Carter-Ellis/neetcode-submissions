#
#               Course  :  Must take these courses to take
#   adjList = { 0 : [1,2], 2 : [0]}
#
#
#
#
#

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create ajdacency list
        adjList = {i : [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        visited = set()

        def dfs(crs):
            # Found a cycle
            if crs in visited:
                return False

            # No cycle found
            if adjList[crs] == []:
                return True

            # Add node to visited
            visited.add(crs)

            # Continue traversing graph
            for pre in adjList[crs]:
                if not dfs(pre):
                    return False
            
            # After traversing those prerequisites we can unmark them as visited just in case another parent needs to traverse through them.
            visited.remove(crs)

            # Already checked all prerequisites for this course so we can remove them
            adjList[crs] = []

            return True
        
        for crs in adjList:
            if not dfs(crs):
                return False
        return True
