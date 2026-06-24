class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if n < 2:
            return n
        

        l, r = 0, 0

        temp = {}

        res = 0

        while r < n:
            if s[r] in temp:
                l = max(temp[s[r]] + 1, l)

            temp[s[r]] = r
            res = max(res, r - l + 1)
            r += 1


        return res

        
            




        