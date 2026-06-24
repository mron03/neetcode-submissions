class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        l = 0
        r = n * len(matrix[0]) - 1  # total elements - 1

        while l <= r:
            pointer = (r + l) // 2
            val = matrix[pointer // len(matrix[0])][pointer % len(matrix[0])]

            if val == target:
                return True

            elif val > target:
                r = pointer - 1
            
            else:
                l = pointer + 1
        
        return False