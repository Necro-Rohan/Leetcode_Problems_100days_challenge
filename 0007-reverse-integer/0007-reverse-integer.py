class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        negative = x < 0
        x = abs(x)
        while x>0:
            reverse = reverse * 10 + x % 10
            x//=10

        if negative:
            reverse = -reverse
        return reverse if pow(-2,31) <= reverse <= pow(2,31)-1 else 0

        