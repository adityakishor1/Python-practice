class Solution(object):
    def maxProduct(self, nums):
        if not nums: return 0
        
        maxLast = nums[0]
        minLast = nums[0]
        ans = nums[0]
        
        for i in xrange(1, len(nums)):
            if nums[i]==0:
                newMax = 0
                newMin = 0
            elif nums[i]>0:
                newMax = maxLast*nums[i] if maxLast>0 else nums[i]
                newMin = minLast*nums[i] if minLast<=0 else nums[i]
            else:
                newMax = minLast*nums[i] if minLast<=0 else nums[i]
                newMin = maxLast*nums[i] if maxLast>0 else nums[i]
            
            maxLast = newMax
            minLast = newMin
            ans = max(ans, maxLast)
            
        return ans
