class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []
        def rec(r, c, visited, prevHeight):
            if (r, c) in visited or r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[r][c] < prevHeight:
                return
            visited.add((r, c))
            rec(r + 1, c, visited, heights[r][c])
            rec(r - 1, c, visited, heights[r][c])
            rec(r, c + 1, visited, heights[r][c])
            rec(r, c - 1, visited, heights[r][c])

        for c in range(COLS):
            rec(0, c, pac, heights[0][c])
            rec(ROWS - 1, c, atl, heights[ROWS - 1][c])
        for r in range(ROWS):
            rec(r, 0, pac, heights[r][0])
            rec(r, COLS - 1, atl, heights[r][COLS - 1])
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res