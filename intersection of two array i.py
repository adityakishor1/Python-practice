class Solution(object):
    def intersection(self, nums1, nums2):
        d1 = {}
        d2 = {}
        for n1 in nums1:
            d1[n1] = 0
        
        for n2 in nums2:
            if n2 in d1:
                d2[n2] = 0
        
        return d2.keys()
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
