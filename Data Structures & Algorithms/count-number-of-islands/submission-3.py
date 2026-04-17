#
#
#   Input: grid = []
#
#   Output: Count of islands
#
#   
#
#   Alogrithm: BFS or DFS
#
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        
        def dfs(row, col):
            if row >= ROWS or col >= COLS or row < 0 or col < 0 or grid[row][col] == "0":
                return
            grid[row][col] = "0"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
                    
        return count