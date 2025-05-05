class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum_count = {0:1}
        pre_sum = 0
        count = 0
        for num in nums:
            pre_sum += num
            if pre_sum - k in pre_sum_count:
                count += pre_sum_count[pre_sum - k]
            if pre_sum in pre_sum_count:
                pre_sum_count[pre_sum] += 1
            else:
                pre_sum_count[pre_sum] = 1
        return count