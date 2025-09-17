class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def helper(amount, idx):
            if amount < 0 or idx >= len(coins):
                return float('inf')
            
            if amount == 0:
                return 0 
            
            if (idx, amount) in memo:
                return memo[(idx, amount)]
            
            take = 1 + helper(amount - coins[idx], idx)
            not_take = helper(amount, idx+1)
            memo[(idx, amount)] = min(take, not_take)
            return memo[(idx, amount)]

        ans = helper(amount, 0)
        return ans if ans != float('inf') else return -1
        