class Solution:
    def numSteps(self, s: str) -> int:
        length = len(s)
        step = 0
        carry = 0
        for i in range(length - 1, 0, -1):
            bit = int(s[i])

            if bit+carry == 1:  # odd
                step+=2       # +1 then divide
                carry = 1
            else:
                step += 1
        
        return step+carry