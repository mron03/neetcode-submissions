class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    count += 1

        
        res = 0
        while q:
            newq = deque()

            while q:
                r, c = q.popleft()

                #bottom
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    newq.append((r - 1, c))
                #up
                if r + 1 < rows and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    newq.append((r + 1, c))
                #left
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    newq.append((r, c - 1))
                #right
                if c + 1 < cols and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    newq.append((r, c + 1))

            if len(newq) > 0:
                res += 1
            
            q = newq

            count -= len(newq)

        
        if count != 0:
            return -1

        return res


