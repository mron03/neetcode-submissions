class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for el in nums:
            freq[el] += 1
        

        buckets = [[] for _ in range(len(nums))]


        for key, v in freq.items():
            buckets[v - 1].append(key)

        res = []

        for bucket in buckets[::-1]:
            for el in bucket:
                res.append(el)

                if len(res) == k:
                    return res