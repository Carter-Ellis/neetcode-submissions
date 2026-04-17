class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        visit = []
        def recRows(r, c, visited, matrix, i):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            if matrix[r][c] != 0:
                visited.append((r, c))
            matrix[r][c] = 0
            recRows(r + i, c, visited, matrix, i)
        def recCols(r, c, visited, matrix, i):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            if matrix[r][c] != 0:    
                visited.append((r, c))
            print(matrix[r][c])
            matrix[r][c] = 0
            print(f"after: {matrix[r][c]}")
            recCols(r, c + i, visited, matrix, i)
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0 and (r, c) not in visit:
                    recRows(r, c, visit, matrix, 1)
                    recRows(r, c, visit, matrix, -1)
                    recCols(r, c, visit, matrix, 1)
                    recCols(r, c, visit, matrix, -1)