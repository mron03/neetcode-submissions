class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if visited[r][c] == 1:
                return
            if grid[r][c] == "0":
                return
            
            visited[r][c] = 1
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        result = 0
        
        for r in range(rows):
            for c in range(cols):
                if visited[r][c] == 0:
                    if grid[r][c] == "0":
                        continue
                    if grid[r][c] == "1":
                        dfs(r, c)
                        result += 1
        
        return result