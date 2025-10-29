class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy_at = float('inf')
        sell_profit = []
        profit = 0
        for i in range(n):
            if prices[i] < buy_at:
                buy_at = prices[i]
            profit = max(profit, prices[i] - buy_at)
            sell_profit.append(profit)
        

        sell_at = float('-inf')
        buy_profit = [0]*n
        for j in range(n-1, -1, -1):
            if prices[j] > sell_at:
                sell_at = prices[j]
            buy_profit[j] = (sell_at - prices[j])
        
        max_profit = 0
        for i in range(n):
            max_profit = max((buy_profit[i] + sell_profit[i]), max_profit)
        return max_profit



            
        