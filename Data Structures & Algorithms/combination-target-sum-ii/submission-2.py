class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []

        def dfs(i, remaining):
            if remaining == 0:
                res.append(subset.copy())
                return
            if i == len(candidates) or candidates[i] > remaining:
                return  # sorted, so no candidate from here on can fit either

            # include candidates[i]
            subset.append(candidates[i])
            dfs(i + 1, remaining - candidates[i])
            subset.pop()

            # skip all duplicates of candidates[i] at this level
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, remaining)

        dfs(0, target)
        return res