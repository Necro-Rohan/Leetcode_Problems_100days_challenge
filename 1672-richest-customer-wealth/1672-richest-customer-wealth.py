class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        n = len(accounts)
        m = len(accounts[0])
        max_amo = 0
        for i in range(n):
            max_amo = max(max_amo, sum(accounts[i]))
        
        return max_amo

        