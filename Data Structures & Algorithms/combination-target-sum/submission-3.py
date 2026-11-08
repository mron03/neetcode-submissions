class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, cur, total):
            if i == len(nums) or total > target:
                return

            if total == target:
                nonlocal result
                result.append(cur.copy())
                return

            cur.append(nums[i])
            total += nums[i]
            dfs(i, cur, total)

            cur.pop()
            total -= nums[i]
            dfs(i + 1, cur, total)


        dfs(0, [], 0)

        return result

