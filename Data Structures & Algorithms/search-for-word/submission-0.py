class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        def search(r, c, currStr):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visited or len(currStr) > len(word):
                return False
            currStr = currStr + board[r][c]
            if currStr == word:
                return True
            visited.add((r, c))
            found = (search(r + 1, c, currStr) or
            search(r, c + 1, currStr) or
            search(r - 1, c, currStr) or
            search(r, c - 1, currStr))
            visited.remove((r, c))
            return found
        for r in range(ROWS):
            for c in range(COLS):
                if search(r, c, ""):
                    return True
        return False
