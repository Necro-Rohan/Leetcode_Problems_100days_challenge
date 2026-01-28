class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            res = target - num
            if res in num_dict.keys():
                return [num_dict[res], i]
            num_dict[num] = i