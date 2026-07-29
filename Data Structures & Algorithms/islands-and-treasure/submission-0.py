class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        visited = set()
        step = 0
        while q:
            new_q = deque()

            while q:
                r, c = q.popleft()

                if (r, c) not in visited and grid[r][c] != -1:
                    visited.add((r, c))

                    grid[r][c] = min(grid[r][c], step)

                    #bottom
                    if r - 1 >= 0:
                        new_q.append((r - 1, c))
                    #up
                    if r + 1 < ROWS:
                        new_q.append((r + 1, c))
                    #left
                    if c - 1 >= 0:
                        new_q.append((r, c - 1))
                    #right
                    if c + 1 < COLS:
                        new_q.append((r, c + 1))

            q = new_q
            step += 1



                    
        