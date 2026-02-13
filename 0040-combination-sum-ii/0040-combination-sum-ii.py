class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(idx, target, cur_arr):
            if target == 0:
                res.append(cur_arr[:])
                return 
            
            for i in range(idx, len(candidates)):
                if candidates[i] > target:
                    break

                if i > idx and candidates[i] == candidates[i-1]:
                    continue  

                cur_arr.append(candidates[i])
                backtrack(i+1, target - candidates[i], cur_arr)
                cur_arr.pop()

        backtrack(0, target, [])
        return res