class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        remainder_count = {0:1} 

        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k

            # If this remainder has been seen before, it means there are subarrays
        # ending at this index which are divisible by K  i.e 5%2 = 1 and (5+2)%2 = 1. here 2 is divisible by 2
            if remainder in remainder_count:
                count+=remainder_count[remainder]
                remainder_count[remainder]+=1
            else:
                remainder_count[remainder] = 1
        
        return count
        