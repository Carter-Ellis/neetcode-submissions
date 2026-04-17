class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        queue = deque()
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in neighbors:
                    newRow = dr + r
                    newCol = dc + c
                    if (min(newRow, newCol) < 0 or newRow >= ROWS or newCol >= COLS or 
                        (newRow, newCol) in visited or grid[newRow][newCol] == 0 or grid[newRow][newCol] == 2):
                        continue
                    queue.append((newRow, newCol))
                    visited.add((newRow, newCol))
            if queue:
                minutes += 1

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 1:
                    return -1
                     
        return minutes
