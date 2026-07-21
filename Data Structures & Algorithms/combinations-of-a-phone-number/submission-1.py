class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        sub = []
        n = len(digits)

        def dfs(i):
            if i == n or len(sub) == n:
                res.append("".join(sub))
                return

            for c in digitToChar[digits[i]]:
                sub.append(c)
                dfs(i + 1)
                sub.pop()
            
        dfs(0)
        return res
            