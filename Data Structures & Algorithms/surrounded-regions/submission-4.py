class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def mark_os(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != 'O':
                return

            board[r][c] = 'M'

            mark_os(r - 1, c)
            mark_os(r + 1, c)
            mark_os(r, c - 1)
            mark_os(r, c + 1)

        for r in range(ROWS):
            for c in range(COLS):
                if (r in [0, ROWS - 1] or c in [0, COLS - 1]) and board[r][c] == 'O':
                    mark_os(r, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'M':
                    board[r][c] = 'O'
