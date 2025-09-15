class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob2(start, end):
            memo = {}
            def helper(idx):
                if idx < start:
                    return 0

                if idx in memo:
                    return memo[idx]
                take = nums[idx] + helper(idx-2)
                skip = helper(idx-1)
                
                memo[idx] =  max(take, skip)
                return memo[idx]
            return helper(end)
        return max(rob2(0,len(nums)-2), rob2(1,len(nums)-1))
