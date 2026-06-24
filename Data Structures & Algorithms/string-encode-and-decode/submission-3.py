class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''

        for s in strs:
            res = res + f"#{str(len(s))}#"
            res += s
        
        return res
        

    def decode(self, s: str) -> List[str]:
        res = []
        print(s)
        
        i = 0
        while i < len(s):
            print(i)
            if s[i] == '#':
                print(s[i])
                i += 1
                length = ''

                while s[i] != '#':
                    length += s[i]
                    i += 1
                    print(length)
                    print(i)

                
                length = int(length)
                res.append(s[i+1: i + 1 + length])
                i += length
                print(res)
                print(i)

            i+=1
        return res
            




