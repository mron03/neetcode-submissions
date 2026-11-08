class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pacifics = set()
        atlantics = set()

        for i in range(ROWS):
            pacifics.add((i, 0))
            atlantics.add((i, COLS - 1))
        
        for i in range(COLS):
            pacifics.add((0, i))
            atlantics.add((ROWS - 1, i))

        def bfs(ocean):
            directions = [(-1,0), (0, -1), (1, 0), (0, 1)]

            queue = ocean.copy()

            while queue:
                new_queue = set()

                for r, c in queue:
                    for dr, dc in directions:
                        dr = r + dr
                        dc = c + dc

                        if (
                            0 <= dr < ROWS and 
                            0 <= dc < COLS and 
                            (dr, dc) not in ocean and 
                            heights[dr][dc] >= heights[r][c]
                        ):
                            new_queue.add((dr, dc))
                            ocean.add((dr, dc))
            
                queue = new_queue
            return ocean
        
        return [list(item) for item in bfs(pacifics) & bfs(atlantics)]
