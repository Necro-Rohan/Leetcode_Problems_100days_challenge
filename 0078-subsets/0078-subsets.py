class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def recurse(nums, current_idx, current_subset, all_subsets):
            if current_idx >= len(nums):
                all_subsets.append(current_subset)
                return
            recurse(nums, current_idx+1 , current_subset + [nums[current_idx]], all_subsets)
            recurse(nums, current_idx+1, current_subset, all_subsets)
        all_subsets = []
        recurse(nums, 0, [], all_subsets)
        return all_subsets
        