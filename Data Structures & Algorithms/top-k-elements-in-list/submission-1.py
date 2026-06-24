class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1

        dic_sorted = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}

        return list(dic_sorted.keys())[-k:]
        
        

        