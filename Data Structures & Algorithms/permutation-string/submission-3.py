class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        f1 = [0] * 26
        for c in s1:
            f1[ord(c) - ord('a')] += 1
        
        l, r = 0, len(s1)

        while r <= len(s2):
            f2 = [0] * 26
            print(l, r)
            for c in s2[l:r]:
                f2[ord(c) - ord('a')] += 1

            if f1 == f2: return True

            l, r = l + 1, r + 1                

        return False