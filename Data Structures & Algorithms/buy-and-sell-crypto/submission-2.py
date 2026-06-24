class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        
        l, r, res = 0, 1, 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            res = max(res, profit)

            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                r += 1
        
        return res