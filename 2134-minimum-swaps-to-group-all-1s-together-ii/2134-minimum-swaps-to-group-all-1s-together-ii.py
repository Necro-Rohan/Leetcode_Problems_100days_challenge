class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total_ones = sum(nums)
        if total_ones <= 1 or total_ones == n:
            return 0
        
        extended_arr = nums + nums

        zeros = total_ones - sum(extended_arr[:total_ones])
        min_swap = zeros

        for i in range(total_ones, n + total_ones):
            if extended_arr[i] == 0:
                zeros += 1
            if extended_arr[i - total_ones] == 0:
                zeros -= 1

            min_swap = min(min_swap, zeros)
        
        return min_swap
            


