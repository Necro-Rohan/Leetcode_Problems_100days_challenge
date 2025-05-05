class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = len(nums)
        prefix_sum = [0] * l
        for i in range(l):
            if i == 0:
                prefix_sum[i] += nums[i]
            else:
                prefix_sum[i] += nums[i] + prefix_sum[i - 1]
        count = 0
        frequency_dic = {}
        for j in range(l):
            if prefix_sum[j] == k:
                count += 1
            val = prefix_sum[j] - k
            count += frequency_dic.get(val, 0)
            if prefix_sum[j] not in frequency_dic:
                frequency_dic[prefix_sum[j]] = 0
            frequency_dic[prefix_sum[j]] += 1
        return count
