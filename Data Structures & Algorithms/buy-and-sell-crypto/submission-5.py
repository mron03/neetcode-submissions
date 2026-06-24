class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0


        l = 0
        profit = 0

        for r in range(1, len(prices)):
            print(l, r)
            if prices[l] > prices[r]:
                l = r
            
            profit = max(profit, prices[r] - prices[l])
        
        return profit
