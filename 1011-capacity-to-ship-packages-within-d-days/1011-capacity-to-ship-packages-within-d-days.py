class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            days_needed = 1
            current_load = 0
            
            for weight in weights:
                if current_load + weight > capacity:
                    days_needed += 1
                    current_load = weight
                    if days_needed > days:
                        return False
                else:
                    current_load += weight
            
            return True

        left = max(weights)  
        right = sum(weights) 
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid  
            else:
                left = mid + 1  

        return left