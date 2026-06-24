class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join([c.lower() for c in s if c.isalnum()])

        i, j = 0, len(new_s) - 1

        while i < j:
            if new_s[i] != new_s[j]:
                return False
            i += 1
            j -= 1

        return True        