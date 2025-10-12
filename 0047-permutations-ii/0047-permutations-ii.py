class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        used = [False] * n
        def backtrack(curr_arr):
            if len(curr_arr) == n:
                res.append(curr_arr[:])
                return

            prev = None
            for i in range(n):
                if nums[i] != prev and not used[i]:
                    used[i] = True
                    curr_arr.append(nums[i])
                    backtrack(curr_arr)
                    curr_arr.pop()
                    used[i] = False
                    prev = nums[i]
        backtrack([])
        return res
        