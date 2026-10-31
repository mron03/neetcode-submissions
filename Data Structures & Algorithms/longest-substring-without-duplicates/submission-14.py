class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        mp = defaultdict()
        l, r = 0, 0
        res = 0

        while r < len(s):
            if s[r] not in mp:
                res = max(res, r - l + 1)
                mp[s[r]] = r
            else:
                i_x = mp[s[r]]
                while l != i_x + 1:
                    del mp[s[l]]
                    l += 1

                mp[s[r]] = r

            r += 1
        
        return res