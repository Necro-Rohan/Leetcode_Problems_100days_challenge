class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}
        def helper(amount, idx):
            if amount == 0:
                return 1

            if amount < 0 or idx >= n:
                return 0
            
            if (amount, idx) in memo:
                return memo[(amount, idx)]
            
            take = helper(amount-coins[idx], idx)
            not_take = helper(amount, idx+1)
            memo[(amount, idx)] = take+not_take
            return memo[(amount, idx)]
        return helper(amount, 0)
        