class Solution(object):
    def rob(self, nums):
        if not nums: return 0
        if len(nums)==0 or len(nums)==1: return max(nums)
        N = len(nums)
        
        v1 = nums[0]
        v2 = nums[0]
        for i in xrange(2, N-1):
            v1, v2 = max(nums[i]+v2, v1), v1
        
        w1 = nums[1]
        w2 = 0
        for i in xrange(2, N):
            w1, w2 = max(nums[i]+w2, w1), w1
        
        return max(v1, w1)
