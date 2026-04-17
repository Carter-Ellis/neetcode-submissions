#
#
#   Input: m * n grid with heights
#   Output: List of coords where water can flow to Pacific and Atlantic Ocean
#
#   Idea (Brute Force): Loop through every cell and run dfs checking if it can make it to both
#
#

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(row, col, visited, prevHeight) -> List[bool]:
            
            if row < 0 or col < 0:
                return [True, False]
            if row >= ROWS or col >= COLS:
                return [False, True]
            if prevHeight < heights[row][col] or (row, col) in visited:
                return [False, False]

            visited.add((row, col))
            currHeight = heights[row][col]

            isUp = dfs(row + 1, col, visited, currHeight)
            isDown = dfs(row - 1, col, visited, currHeight)
            isRight = dfs(row, col + 1, visited, currHeight)
            isLeft = dfs(row, col - 1, visited, currHeight)
            isPacific = isUp[0] or isDown[0] or isRight[0] or isLeft[0]
            isAtlantic = isUp[1] or isDown[1] or isRight[1] or isLeft[1]
            return [isPacific, isAtlantic]
        
        for r in range(ROWS):
            for c in range(COLS):
                isPacific, isAtlantic = dfs(r, c, set(), heights[r][c])
                if isPacific and isAtlantic:
                    res.append([r, c])
        return res