class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        mp = {
            "]": "[",
            "}": "{",
            ")": "("
        }


        for c in s:
            if c in mp.values():
                st.append(c)
            elif c in mp.keys() and st:
                val = st.pop()
                if val != mp[c]:
                    return False
            else:
                return False
            

        
        return True if not st else False
