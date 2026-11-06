class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        count = defaultdict(int)
        result = 0

        for r in range(len(s)):
            count[s[r]] += 1

            while r - l + 1 - max(count.values()) > k and l < r:
                count[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)

        
        return result
                
