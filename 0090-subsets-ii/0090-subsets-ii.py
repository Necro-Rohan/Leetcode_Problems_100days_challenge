class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def unique_subset(nums, idx, cur_subset, all_subset):
            if idx >= len(nums):
                if sorted(cur_subset) not in all_subset:
                    all_subset.append(sorted(cur_subset))
                return
            unique_subset(nums, idx+1, cur_subset + [nums[idx]], all_subset)
            unique_subset(nums, idx+1, cur_subset, all_subset)
        all_subset = []
        unique_subset(nums, 0, [], all_subset)
        return all_subset
                
        