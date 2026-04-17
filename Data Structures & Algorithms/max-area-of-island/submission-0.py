class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        largestArea = 0
        visitedIslands = set()
        
        def dfs(r, c) -> int:
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r,c) in visitedIslands:
                return 0
            visitedIslands.add((r, c))
            count = 1
            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)
            return count
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visitedIslands:
                    largestArea = max(largestArea, dfs(r,c))
        return largestArea