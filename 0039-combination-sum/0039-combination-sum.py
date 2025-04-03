class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def totalCombination(candidates, target, ans, cur_comb, idx):
            if idx == len(candidates):
                if target == 0:
                    ans.append(list(cur_comb))
                return
            if candidates[idx] <= target:
                cur_comb.append(candidates[idx])
                totalCombination(candidates, target-candidates[idx], ans, cur_comb, idx)
                cur_comb.pop()
            totalCombination(candidates, target, ans, cur_comb, idx+1)
        
        ans = []
        cur_comb = []
        totalCombination(candidates, target, ans, cur_comb, 0)
        return ans
        

