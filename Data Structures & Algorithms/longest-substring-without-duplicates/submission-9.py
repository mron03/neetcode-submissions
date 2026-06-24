class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        dic = {}
        l = 0
        res = 0


        for r in range(len(s)):
            if s[r] not in dic:
                dic[s[r]] = r
            else:
                v = dic[s[r]]
                while l <= v:
                    print(l)
                    dic.pop(s[l])
                    print(dic)
                    l += 1

                dic[s[r]] = r

            res = max(res, r - l + 1)

        return res

