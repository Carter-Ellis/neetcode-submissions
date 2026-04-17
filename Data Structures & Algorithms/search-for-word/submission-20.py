class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])

        def rec(index, row, col, visited)-> bool:
            if  (row, col) in visited or row >= ROW or col >= COL or row < 0 or col < 0:
                print((row, col) in visited)
                return False
            
            if word[index] != board[row][col]:
                return False
            print(f"index: {index}    char: {word[index]}    board: {board[row][col]}   row,col: ({row}, {col})  ")
            if index >= len(word) - 1:
                return True
            
            

            visited.add((row, col))

            if (rec(index + 1, row + 1, col, visited) or
            rec(index + 1, row - 1, col, visited) or
            rec(index + 1, row, col + 1, visited) or
            rec(index + 1, row, col - 1, visited)):
                return True

            visited.remove((row,col))
            print("pop")
        
        for r in range(ROW):
            for c in range(COL):
                if rec(0, r, c, set()):
                    return True
        return False

