class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        arr = [-1] * n

        def dfs(i):

            if i >= n:
                return 0
            
            if arr[i] != -1:
                return arr[i]

            
            left = dfs(i + 1)
            right = dfs(i + 2)

            res =  cost[i] + min(left,  right)

            arr[i] = res

            return res

        return min(dfs(0), dfs(1))
