#
#
# Input: 2D matrix (grid)
#
# Output: # of minutes until there are zero fresh fruits
#
#   Notes:
#       - 0 = empty cell
#       - 1 = fresh fruit
#       - 2 = rotten fruit

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        bananaCount, time = 0, 0

        queue = deque()

        # Counts bananas and gets position of rotten bananas
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    bananaCount += 1
                if grid[r][c] == 2:
                    queue.appendleft((r, c))

        if bananaCount == 0:
            return 0

        newQ = deque()
        print(bananaCount)
        while queue:
            print(queue)
            rotRow, rotCol = queue.pop()
            upPos, downPos, leftPos, rightPos = (rotRow + 1, rotCol), (rotRow - 1, rotCol), (rotRow, rotCol - 1), (rotRow, rotCol + 1)
            pos = (0, 0)
            for i in range(4):
                match i:
                    case 0:
                       pos = upPos
                    case 1:
                        pos = downPos
                    case 2:
                        pos = leftPos
                    case 3:
                        pos = rightPos
                row, col = pos[0], pos[1]
                if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] != 1:
                    continue
                newQ.appendleft(pos)
                grid[row][col] = 2
                bananaCount -= 1
            if not queue:
                queue = newQ.copy()
                newQ = deque()
                time += 1

                if bananaCount == 0:
                    return time
        return -1
