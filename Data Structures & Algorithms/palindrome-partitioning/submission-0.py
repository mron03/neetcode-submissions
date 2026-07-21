class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sub = []

        def is_palindrome(text):
            l, r = 0, len(text) - 1
            while l < r:
                if text[l] != text[r]:
                    return False

                l += 1
                r -= 1
            
            return True

        def dfs(i):
            if i == len(s):
                res.append(sub.copy())

                return

            
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]

                if is_palindrome(substring):
                    sub.append(substring)
                    dfs(j)
                    sub.pop()

        dfs(0)

        return res


