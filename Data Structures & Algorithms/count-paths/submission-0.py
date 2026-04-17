class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def rec(r, c) -> int:
            if r < 0 or c < 0 or r >= m or c >= n:
                return 0
            if (r, c) == ((m-1),(n-1)):
                return 1
            return rec(r + 1, c) + rec(r, c + 1)
        return rec(0,0)
            