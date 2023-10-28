class Solution(object):
    def search(self, nums, target):
        if not nums: return -1

        l = 0
        r = len(nums)-1

        while True:
            if l>r: break
            if target<nums[l]: return -1
            if nums[r]<target: return -1

            if target==nums[l]: return l
            if target==nums[r]: return r

            m = (l+r)/2
            if target==nums[m]:
                return m
            elif target<nums[m]:
                r = m-1
            else:
                l = m+1
        return -1
