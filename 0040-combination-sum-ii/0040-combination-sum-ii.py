class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(idx, target, cur_arr):
            if target == 0:
                res.append(cur_arr[:])
                return 
            
            if idx >= len(candidates) or target < 0:
                return 
            
            cur_arr.append(candidates[idx])
            backtrack(idx+1, target - candidates[idx], cur_arr)
            cur_arr.pop()

            next_idx = idx + 1
            while next_idx < len(candidates) and candidates[next_idx] == candidates[idx]:
                next_idx += 1
            backtrack(next_idx, target, cur_arr)
        backtrack(0, target, [])
        return res