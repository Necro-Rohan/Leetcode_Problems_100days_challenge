class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i, cur_arr):
            if len(cur_arr) == k:
                res.append(cur_arr[:])
                return
            if i > n:
                return 
            
            cur_arr.append(i)
            backtrack(i+1, cur_arr)
            cur_arr.pop()
            backtrack(i+1, cur_arr)
        backtrack(1, [])
        return res
        