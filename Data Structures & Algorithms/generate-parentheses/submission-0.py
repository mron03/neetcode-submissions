class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sub = []
         
        def dfs(open_count, close_count):
            
            if len(sub) == 2 * n:
                res.append("".join(sub))
                return
            
            if open_count < n:
                sub.append("(")
                dfs(open_count + 1, close_count)
                sub.pop()

            if close_count < open_count:
                sub.append(")")
                dfs(open_count, close_count + 1)
                sub.pop()

        dfs(0,0)
        return res