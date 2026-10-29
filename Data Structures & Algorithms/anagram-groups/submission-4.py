class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            freq = [0] * 26

            for c in s:
                freq[ord(c) - ord('a')] += 1

            key = tuple(freq)

            if key not in res:
                res[key] = [s]
            else:
                res[key].append(s)


        return list(res.values())