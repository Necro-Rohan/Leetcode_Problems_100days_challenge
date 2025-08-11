class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[low] = nums[low], nums[i]
                low+=1
        for i in range(low, n):
            if nums[i] == 1:
                nums[i], nums[low] = nums[low], nums[i]
                low+=1
        for i in range(low, n):
            if nums[i] == 2:
                nums[i], nums[low] = nums[low], nums[i]
                low+=1
        return nums