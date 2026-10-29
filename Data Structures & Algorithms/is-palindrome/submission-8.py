class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = set([i for i in range(97, 97+26)] + [i for i in range(47, 58)])

        l, r = 0, len(s) - 1

        while l < r:
            lc = s[l].lower()
            rc = s[r].lower()

            if ord(lc) not in valid:
                l += 1
                continue
            elif ord(rc) not in valid:
                r -= 1
                continue
            
            if lc != rc:
                return False

            l += 1
            r -= 1
        return True
