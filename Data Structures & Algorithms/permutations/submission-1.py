class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sett = [0] * len(nums)
        res = []
        subset = []

        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for i in range(len(nums)):
                if sett[i] == 0:
                    sett[i] = 1
                    subset.append(nums[i])
                    dfs()
                    subset.pop()
                    sett[i] = 0
            
        dfs()

        return res

