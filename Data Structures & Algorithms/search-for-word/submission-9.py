class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(r, c, visited, i):
            if (
                i == len(word) or
                r < 0 or
                c < 0 or
                r >= len(board) or 
                c >= len(board[0]) or 
                (r, c) in visited or
                board[r][c] != word[i]
            ):
                return False
            
            if i == len(word) - 1 and board[r][c] == word[i]:
                return True

            visited.add((r, c))

            found = (
                dfs(r + 1, c, visited, i + 1) or
                dfs(r - 1, c, visited, i + 1) or
                dfs(r, c + 1, visited, i + 1) or
                dfs(r, c - 1, visited, i + 1)
            )

            visited.remove((r,c))

            return found
        

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    visited = set()
                    if dfs(r, c, visited, 0):
                        return True

        
        return False