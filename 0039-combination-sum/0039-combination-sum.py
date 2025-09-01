class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(candidates, target, idx, cur_arr):      
            if target == 0:
                res.append(cur_arr.copy())
                return
            
            if idx >= len(candidates) or target < 0:
                return
            
            cur_arr.append(candidates[idx])
            backtrack(candidates, target - candidates[idx], idx, cur_arr)
            cur_arr.pop()
            backtrack(candidates, target, idx+1, cur_arr)
        backtrack(candidates, target, 0, [])
        return res 
        