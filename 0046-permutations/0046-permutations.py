class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(idx, curr_arr):
            if len(curr_arr) == len(nums):
                res.append(curr_arr[:])
                return 
            
            for i in range(len(nums)):
                if nums[i] in curr_arr:
                    continue
                curr_arr.append(nums[i])
                backtrack(i+1, curr_arr)
                curr_arr.pop()
            return 
        backtrack(0, [])
        return res
        