class Solution:
    def mySqrt(self, n: int) -> int:

        low=0
        high=n
        while low <= high:
            m = (low + high) // 2
            sq_m = m * m 
            if sq_m == n:
                return m
            elif sq_m > n:
                high = m - 1
            else:
                low = m + 1
        else:
            return high