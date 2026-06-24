class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        cubes = [set() for _ in range(n)]


        for i in range(n):
            row = set()
            col = set()

            for j in range(n):
                i_val = board[i][j]
                j_val = board[j][i]
                cube_id = int(i / 3) * 3 + int(j / 3) 

                if i_val != '.':
                    if i_val in row or i_val in cubes[cube_id]:
                        return False
                    
                    row.add(i_val)
                    cubes[cube_id].add(i_val)
                
                if j_val != '.':
                    if j_val in col:
                        return False
                    
                    col.add(j_val)


        return True
                
