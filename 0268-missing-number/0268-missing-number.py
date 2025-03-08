class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        conse_sum = n*(n+1)//2
        total_sum = 0
        for i in range(n):
            total_sum+=nums[i]

        missing = conse_sum - total_sum
        return missing

        
        