class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m - 1, n - 1

        def dfs(r, c, ROWS, COLS):
            
            if r > ROWS or c > COLS:
                return 0
            
            if (r, c) == (ROWS, COLS):
                return 1

            return dfs(r + 1, c, ROWS, COLS) + dfs(r, c + 1, ROWS, COLS)
            
        
        return dfs(0, 0, ROWS, COLS)