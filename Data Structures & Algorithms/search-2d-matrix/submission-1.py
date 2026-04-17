class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowL, rowR = 0, len(matrix) - 1
        
        while rowL <= rowR:
            rowMid = rowL + ((rowR - rowL) // 2)
            print("Hello")
            print(f"Row Mid: {rowMid}")
            colL, colR = 0, len(matrix[0]) - 1
            while colL <= colR:
                colMid = colL + ((colR - colL) // 2)
                print(matrix[rowMid][colMid])
                if target < matrix[rowMid][colMid]:
                    colR = colMid - 1
                elif target > matrix[rowMid][colMid]:
                    colL = colMid + 1
                elif target == matrix[rowMid][colMid]:
                    return True
            if colR < 0:
                rowR = rowMid - 1
            elif colL > len(matrix[0]) - 1:
                rowL = rowMid + 1
            else:
                return False
        return False