class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        width, height = len(matrix[0]), len(matrix)
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        pos = [-1,0]
        index = 0

        ans = []

        while len(ans) < len(matrix[0]) * len(matrix):
            if index == 0 or index == 2:
                for i in range(width):
                    pos[0] += dirs[index][0]
                    ans.append(matrix[pos[1]][pos[0]])
                index = (index + 1) % 4
                height -= 1
            else:
                for i in range(height):
                    pos[1] += dirs[index][1]
                    ans.append(matrix[pos[1]][pos[0]])
                index = (index + 1) % 4
                width -= 1      


        return ans