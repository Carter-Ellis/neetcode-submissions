class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for r in range(9):
            line = {}
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] not in line:
                    line[board[r][c]] = 1
                else:
                    line[board[r][c]] += 1
            for value in line.values():
                if value > 1:
                    return False
        for c in range(9):
            line = {}
            for r in range(9 - 1, -1, -1):
                if board[r][c] == ".":
                    continue
                if board[r][c] not in line:
                    line[board[r][c]] = 1
                else:
                    line[board[r][c]] += 1
            for value in line.values():
                if value > 1:
                    return False

        for i in range(9):
            line = {}
            rowJump = 0
            if i == 2:
                rowJump += 3
            if i == 5:
                rowJump += 3

            for r in range(rowJump, 3 + rowJump):
                for c in range((i*3) % 9, (i*3 + 3) % 9):
                    print(r,c)
                    if board[r][c] == ".":
                        continue
                    if board[r][c] not in line:
                        line[board[r][c]] = 1
                    else:
                        line[board[r][c]] += 1
            for value in line.values():
                if value > 1:
                    return False

        return True