class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = cost[-2]
        two = cost[-1]

        for i in range(len(cost) - 3, -1, -1):
            temp = one
            one = cost[i] + min(one, two)
            two = temp
        
        return min(one, two)