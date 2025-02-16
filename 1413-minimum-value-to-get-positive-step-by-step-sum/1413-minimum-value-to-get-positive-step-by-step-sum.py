class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        total_sum = 0
        start_value = 1
        min_sum = float('inf')
        for i in range(len(nums)):
            total_sum += nums[i]
            min_sum = min(min_sum,total_sum)
        return start_value - min_sum if (start_value - min_sum) > start_value else start_value
        