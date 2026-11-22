class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10,2,5,1]
        if len(prices) == 1:
            return 0

        buy_i, sell_i = 0, 1
        profit = 0
        while sell_i < len(prices):
            if prices[sell_i] > prices[buy_i]:
                profit = max(profit, prices[sell_i] - prices[buy_i])
            else:
                buy_i = sell_i
            sell_i += 1
        return profit
            

        

        


