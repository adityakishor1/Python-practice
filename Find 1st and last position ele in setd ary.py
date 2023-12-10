class Solution(object):
    def searchRange(self, nums, target):
        def find_range(i, nums):
            start = end = i
            while 0<=start-1 and nums[start-1]==nums[i]:
                start -= 1
            while end+1<len(nums) and nums[end+1]==nums[i]:
                end += 1
            return [start, end]
            
        
        if not nums: return [-1, -1]
        l = 0
        r = len(nums)-1

        while True:
            if l>r: break
            if target<nums[l]: return [-1, -1]
            if target>nums[r]: return [-1, -1]

            if target==nums[l]: return find_range(l, nums)
            if target==nums[r]: return find_range(r, nums)

            m = (l+r)/2
            if target==nums[m]:
                return find_range(m, nums)
            elif target<nums[m]:
                r = m-1
            else:
                l = m+1
        
        return [-1, -1]
