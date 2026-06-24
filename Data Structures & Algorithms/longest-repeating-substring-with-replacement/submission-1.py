class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {chr(i): 0 for i in range(ord('A'), ord('A') + 26)}

        res, l = 0, 0

        for r in range(len(s)):
            count[s[r]] += 1

            window_size = r - l + 1

            to_replace = window_size - max(count.values())

            if to_replace <= k:
                res = window_size
            else:
                count[s[l]] -= 1
                l += 1
        
        return res


