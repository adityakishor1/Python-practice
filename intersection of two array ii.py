class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        
        i = j = 0
        ans = []
        
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                ans.append(nums1[i])
                i += 1
                j +=1
            elif nums1[i]>nums2[j]:
                j += 1
            else:
                i += 1
        return ans
