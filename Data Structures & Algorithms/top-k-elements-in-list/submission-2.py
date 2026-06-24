class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}


        for n in nums:
            dic[n] = 1 + dic.get(n, 0)
        

        arr = [[] for i in range(len(nums) + 1)]

        print(arr)
        print(dic)
        for key, v in dic.items():
            print(v)

            arr[v].append(key)

        res = []
        print(dic)
        print(arr)

        for i in range(len(arr)-1, 0, -1):
            res.extend(arr[i])
            print(len(res), k, "here")
            if len(res) == k:
                return res
            


        