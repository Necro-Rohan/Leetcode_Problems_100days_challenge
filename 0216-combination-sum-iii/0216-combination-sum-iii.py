class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(start, cur_arr, cur_sum):
            if len(cur_arr) == k:
                if cur_sum == n:
                    res.append(cur_arr[:])
                return 
            
            if len(cur_arr) > k or cur_sum > n or start > 9:
                return 
            
            cur_arr.append(start)
            backtrack(start+1, cur_arr, cur_sum+start)
            cur_arr.pop()
            backtrack(start+1, cur_arr, cur_sum)
        backtrack(1, [], 0)
        return res
            



        