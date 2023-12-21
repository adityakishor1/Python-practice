class Solution(object):
    def firstMissingPositive(self, nums):
        N = len(nums)
        
        if 1 not in nums: return 1
        
        for i, num in enumerate(nums):
            if num<=0 or num>N:
                nums[i] = 1
        
        for i in xrange(N):
            a = abs(nums[i])
            
            if a==N:
                nums[0] = -abs(nums[0])
            else:
                nums[a] = -abs(nums[a])
        
        for i in xrange(1, N):
            if nums[i]>0: return i
        if nums[0]>0: return N
        
        return N+1
