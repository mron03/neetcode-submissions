class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_strs = ["".join(sorted(s)) for s in strs]
        dic = {}

        for i, s in enumerate(sorted_strs):
            if s in dic:
                dic[s] += [strs[i]]
            else:
                dic[s] = [strs[i]]
    
        return [val for val in dic.values()]



            
            
