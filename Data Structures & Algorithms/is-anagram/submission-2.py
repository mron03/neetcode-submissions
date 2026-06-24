class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dic_s = {}
        dic_t = {}

        def count_frequency(s: str):
            dic = {}

            for c in s:
                if c in dic:
                    dic[c] += 1
                else:
                    dic[c] = 1

            return dic

        dic_s = count_frequency(s)
        dic_t = count_frequency(t)

        return dic_s == dic_t