class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visitedIslands = set()
        def dfs(r, c):          
            if (r, c) in visitedIslands or (r, c) in visitedIslands or min(r, c) < 0 or r >= ROWS or c >= COLS:    
                return 0
            if grid[r][c] == "0":
                return 0
            visitedIslands.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return 1
        result = 0
        for row in range(ROWS):
            for col in range(COLS):
                result += dfs(row,col)
        return result