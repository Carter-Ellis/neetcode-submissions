class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrixL, matrixR = 0, len(matrix) - 1       

        while matrixL <= matrixR:
            matrixM = (matrixL + matrixR) // 2
            l, r = 0, len(matrix[0]) - 1
            
            while l <= r:
                m = (l + r) // 2
                if matrix[matrixM][m] < target:
                    l = m + 1
                    if l > r:
                        matrixL = matrixM + 1
                        break
                elif matrix[matrixM][m] > target:
                    r = m - 1
                    if l > r:
                        matrixR = matrixM - 1
                        break
                else:
                    return True          
        
        return False
                

