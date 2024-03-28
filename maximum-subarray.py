class Solution(object):
    def maxSubArray(self, nums):
        ans = nums[0]
        last_max = nums[0]
        
        for i in xrange(len(nums)):
            if i==0: continue
            last_max = max(nums[i], nums[i]+last_max)
            ans = max(ans, last_max)
            
        return ans
