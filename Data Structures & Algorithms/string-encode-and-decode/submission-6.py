class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(str(len(s))+ '#' + s for s in strs)
        

    def decode(self, s: str) -> List[str]:
        i, res = 0, []
        
        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            word_len = int(s[i:j])

            res.append(s[j + 1: j + 1 + word_len])

            i = j + 1 + word_len
        return res
            




