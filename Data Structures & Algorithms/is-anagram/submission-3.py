from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_s = Counter(s)
        counter_t = Counter(t)
        

        if len(counter_s) != len(counter_t):
            return False

            
        for s_c in counter_s.keys():
            if s_c not in counter_t or counter_s[s_c] != counter_t[s_c]:
                return False
        

        return True

            

        