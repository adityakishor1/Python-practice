class Solution(object):
    def rob(self, nums):
        if not nums: return 0
        if len(nums)==0 or len(nums)==1: return max(nums)
        
        last1 = max(nums[0], nums[1])
        last2 = nums[0]
        
        for i in xrange(len(nums)):
            if i==0 or i==1: continue
            last2, last1 = last1, max(nums[i]+last2, last1)
            
        return last1
