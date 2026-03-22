class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        summ = 0
        
        while n > 0:
            digit = n % 10
            prod *= digit
            summ += digit
            n //= 10
        
        return prod - summ