class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}

        for s in strs:
            ss = "".join(sorted(s))

            if ss not in freq:
                freq[ss] = [s]
            else:
                freq[ss].append(s)

        
        return list(freq.values())