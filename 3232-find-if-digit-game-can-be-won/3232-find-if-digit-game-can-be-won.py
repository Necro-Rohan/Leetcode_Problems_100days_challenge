class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_dig = 0
        double_dig = 0
        for i in nums:
            if i//10 >= 1:
                double_dig += i
            else:
                single_dig += i 
        
        return not single_dig == double_dig
        