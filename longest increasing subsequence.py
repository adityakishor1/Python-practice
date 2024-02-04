class Solution(object):
    def lengthOfLIS(self, nums):
        dp = [1]*len(nums)
        
        for i in xrange(1, (len(nums))):
            for j in xrange(i-1, -1, -1):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)
