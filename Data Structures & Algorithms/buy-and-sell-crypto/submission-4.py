class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10, 2, 5, 1, 22]
        #profit = sell - buy
        profit = 0
        l = 0
        r = 1
        while r < len(prices):
            dif = prices[r] - prices[l]
            if dif < 0:
                l = r
            profit = max(dif, profit)
            r += 1
        return profit
        


