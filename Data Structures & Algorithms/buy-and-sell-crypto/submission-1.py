class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1:
            return 0

        
        l, r = 0, 1

        res = 0


        while r < len(prices):

            profit = prices[r] - prices[l]
            res = max(res, profit)
            print(prices[l], prices[r], res)

            if prices[r] < prices[l]:
                l = r
                r += 1
            elif profit == res:
                r += 1
            elif profit > res:
                res = profit
                r += 1
            else:
                r += 1
        



        return res