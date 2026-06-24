class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        cubes = [set() for _ in range(n)]


        for i in range(n):
            row = set()
            col = set()

            for j in range(n):
                row_val = board[i][j]
                col_val = board[j][i]
                cube_id = int(i / 3) * 3 + int(j / 3) 

                if row_val != '.':
                    if row_val in row or row_val in cubes[cube_id]:
                        return False
                    
                    row.add(row_val)
                    cubes[cube_id].add(row_val)
                
                if col_val != '.':
                    if col_val in col:
                        return False
                    
                    col.add(col_val)


        return True
                
