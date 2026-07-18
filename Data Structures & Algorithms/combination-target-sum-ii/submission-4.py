class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        nums = sorted(candidates)

        def dfs(i):
            if sum(subset) == target:
                res.append(subset.copy())
                return

            if i == len(nums) or sum(subset) > target:
                return

            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1)

        
        dfs(0)
        return res
