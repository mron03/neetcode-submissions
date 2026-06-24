class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"#{len(s)}#{s}" for s in strs)
        

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        
        while i < len(s):
            if s[i] == '#':
                i += 1
                word_len = ''

                while s[i] != '#':
                    word_len += s[i]
                    i += 1
                
                word_len = int(word_len)
                res.append(s[i + 1: i + 1 + word_len])
                i += word_len

            i+=1
        return res
            




