class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = float('inf')
        profit = 0
        for i in range(n):
            if prices[i] < buy:
                buy = prices[i]

            profit = max(profit, prices[i]-buy)
        
        return profit

        