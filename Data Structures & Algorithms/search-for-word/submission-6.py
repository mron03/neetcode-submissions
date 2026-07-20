class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        tag = set()

        def helper(i, j, ch_index):
            if ch_index == len(word):
                return True

            if j - 1 >= 0 and (i, j - 1) not in tag:
                if word[ch_index] == board[i][j - 1]:
                    tag.add((i, j - 1))
                    if helper(i, j - 1, ch_index + 1):
                        return True

                    tag.remove((i, j - 1))
            
            if j + 1 < len(board[0]) and (i, j + 1) not in tag:

                if word[ch_index] == board[i][j + 1]:
                    tag.add((i, j + 1))
                
                    if helper(i, j + 1, ch_index + 1):
                        return True
                    
                    tag.remove((i, j+ 1))
            
            if i - 1 >= 0 and (i - 1, j) not in tag:
                if word[ch_index] == board[i - 1][j]:
                    tag.add((i - 1, j))
                    
                    if helper(i - 1, j, ch_index + 1):
                        return True

                    tag.remove((i-1, j))
            
            if i + 1 < len(board) and (i + 1, j) not in tag:
                if word[ch_index] == board[i + 1][j]:
                    tag.add((i + 1, j))

                    if helper(i + 1, j, ch_index + 1):
                        return True
                    tag.remove((i+1, j))

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    tag.add((i,j))
                    if helper(i, j, 1): 
                        return True
                    tag = set()

        return False
                