class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        for i in range(n):
            if i!= 0:
                prefix[i] = prefix[i-1] + nums[i]
            else:
                prefix[i] = nums[i]
        return prefix
        