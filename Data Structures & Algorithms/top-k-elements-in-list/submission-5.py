class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)

        for el in nums:
            res[el] += 1
        
        return [y[0] for y in sorted(list(res.items()), key=lambda x: x[1], reverse=True)[:k]]