class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s, left, right):
            # s = current string
            # left = number of '(' used
            # right = number of ')' used
            
            if len(s) == 2 * n:
                res.append(s)
                return
            
            if left < n:
                backtrack(s + "(", left + 1, right)
            
            if right < left:
                backtrack(s + ")", left, right + 1)

        backtrack("", 0, 0)
        return res