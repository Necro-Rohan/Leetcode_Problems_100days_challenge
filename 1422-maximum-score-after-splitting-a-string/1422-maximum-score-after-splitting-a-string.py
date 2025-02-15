class Solution:
    def maxScore(self, s: str) -> int:
        left = 0
        right = s.count('1')
        max_score = 0
        for i in range(len(s)-1):
            if s[i]=='0':
                left+=1
            else:
                right-=1
            max_score = max(max_score,left+right)
        return max_score
        