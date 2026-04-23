"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        visited = {}

        newNode = Node(node.val)
        visited[node] = newNode

        def dfs(curr, newNode):
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    newNeighbor = Node(neighbor.val)
                    visited[neighbor] = newNeighbor
                    
                    newNode.neighbors.append(newNeighbor)
                    dfs(neighbor, newNeighbor)
                else:
                    newNode.neighbors.append(visited[neighbor])

        dfs(node, newNode)
        return newNode
