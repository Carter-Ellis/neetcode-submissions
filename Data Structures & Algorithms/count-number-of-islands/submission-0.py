class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visitedIslands = set()
        def dfs(r, c, visited):          
            if (r, c) in visited or (r, c) in visitedIslands or min(r, c) < 0 or r >= ROWS or c >= COLS:    
                return 0
            if grid[r][c] == "0":
                return 0
            visited.add((r, c))
            visitedIslands.add((r, c))
            dfs(r + 1, c, visited)
            dfs(r - 1, c, visited)
            dfs(r, c + 1, visited)
            dfs(r, c - 1, visited)
            visited.remove((r, c))
            return 1
        result = 0
        for row in range(ROWS):
            for col in range(COLS):
                print("Yo")
                result += dfs(row,col,set())
        return result