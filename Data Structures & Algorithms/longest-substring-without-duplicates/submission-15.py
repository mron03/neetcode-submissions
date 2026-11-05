class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l = 0 
        hashmap = defaultdict(int)
        res = 0

        for r in range(len(s)):
            if s[r] in hashmap:
                while l <= hashmap[s[r]]:
                    del hashmap[s[l]]
                    l += 1
                
            
            hashmap[s[r]] = r
            res = max(res, r - l + 1)

        
        return res



            