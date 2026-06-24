class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        temp = {}

        for r in range(len(s)):
            if s[r] in temp:
                l = max(temp[s[r]] + 1, l)

            temp[s[r]] = r
            res = max(res, r - l + 1)

        return res
