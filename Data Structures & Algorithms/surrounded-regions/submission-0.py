class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS, = len(board), len(board[0])


        def dfsCheck(row, col, visited) -> bool:

            if row >= ROWS or row < 0 or col >= COLS or col < 0:
                return False

            if board[row][col] == "X" or (row, col) in visited:
                return True

            visited.add((row, col))
            return (dfsCheck(row + 1, col, visited) 
                and dfsCheck(row - 1, col, visited) 
                and dfsCheck(row, col + 1, visited) 
                and dfsCheck(row, col - 1, visited))

        def dfsFlip(row, col):
            if row >= ROWS or row < 0 or col >= COLS or col < 0 or board[row][col] == "X":
                return
            board[row][col] = "X"

            dfsFlip(row + 1, col) 
            dfsFlip(row - 1, col) 
            dfsFlip(row, col + 1) 
            dfsFlip(row, col - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if dfsCheck(r, c, set()):
                    dfsFlip(r, c)
        