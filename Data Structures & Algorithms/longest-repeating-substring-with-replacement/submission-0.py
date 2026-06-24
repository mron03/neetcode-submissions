class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {chr(i): 0 for i in range(ord('A'), ord('A') + 26)}

        res, l = 0, 0

        for r in range(len(s)):
            count[s[r]] += 1

            leftover = (r - l + 1) - max(count.values())

            if leftover <= k:
                res = max(res, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1
        
        return res


