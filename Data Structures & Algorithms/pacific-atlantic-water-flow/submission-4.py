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

        pac_queue = pacifics.copy()
        atl_queue = atlantics.copy()


        while pac_queue:
            new_queue = set()

            for r, c in pac_queue:
                if (
                    r + 1 < ROWS and 
                    (r + 1, c) not in pacifics and 
                    heights[r + 1][c] >= heights[r][c]
                ):
                    new_queue.add((r + 1, c))
                    pacifics.add((r + 1, c))
                
                if (
                    c + 1 < COLS and 
                    (r, c + 1) not in pacifics and 
                    heights[r][c + 1] >= heights[r][c]
                ):
                    new_queue.add((r, c + 1))
                    pacifics.add((r, c + 1))

                if (
                    r - 1 >= 0 and 
                    (r - 1, c) not in pacifics and 
                    heights[r - 1][c] >= heights[r][c]
                ):
                    new_queue.add((r - 1, c))
                    pacifics.add((r - 1, c))

                if (
                    c - 1 >= 0 and 
                    (r, c - 1) not in pacifics and 
                    heights[r][c - 1] >= heights[r][c]
                ):
                    new_queue.add((r, c - 1))
                    pacifics.add((r, c - 1))

                
            
            pac_queue = new_queue
        
        while atl_queue:
            new_queue = set()

            for r, c in atl_queue:
                if (
                    r - 1 >= 0 and 
                    (r - 1, c) not in atlantics and 
                    heights[r - 1][c] >= heights[r][c]
                ):
                    new_queue.add((r - 1, c))
                    atlantics.add((r - 1, c))
                if (
                    c - 1 >= 0 and 
                    (r, c - 1) not in atlantics and 
                    heights[r][c - 1] >= heights[r][c]
                ):
                    new_queue.add((r, c - 1))
                    atlantics.add((r, c - 1))
                
                if (
                    r + 1 < ROWS and 
                    (r + 1, c) not in atlantics and 
                    heights[r + 1][c] >= heights[r][c]
                ):
                    new_queue.add((r + 1, c))
                    atlantics.add((r + 1, c))
                if (
                    c + 1 < COLS and 
                    (r, c + 1) not in atlantics and 
                    heights[r][c + 1] >= heights[r][c]
                ):
                    new_queue.add((r, c + 1))
                    atlantics.add((r, c + 1))


            atl_queue = new_queue

        return [list(item) for item in atlantics & pacifics]
