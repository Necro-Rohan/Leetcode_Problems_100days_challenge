class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0
        intersection_arr = set()
        while i < n and j < m:
            if nums1[i] == nums2[j]:
                intersection_arr.add(nums1[i])
                i+=1
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        return list(intersection_arr)

        