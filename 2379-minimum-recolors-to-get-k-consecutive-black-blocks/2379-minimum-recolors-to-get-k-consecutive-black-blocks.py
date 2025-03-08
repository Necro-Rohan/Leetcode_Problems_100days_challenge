class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        j = 0
        coloring = float('inf')
        white = 0
        for i in range(n):       
            if blocks[i] == 'W':
                white+=1
            while i == k+j-1:
                coloring = min(coloring,white)
                if blocks[j] == 'W':
                    white -= 1                
                j+=1
        return coloring
                
