class Solution:
    def get_hour(self, piles: List[int], k: int) -> int:
        hour = 0
        for i in piles:
            hour += (i + k - 1) // k  
        return hour 

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while low < high:
            mid = (low + high) // 2
            if self.get_hour(piles, mid) <= h:
                high = mid
            else:
                low = mid + 1

        return low

    