class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ans = []
        N = len(nums)
        
        for i in xrange(N):
            j = i+1
            k = N-1
            
            if i>0 and nums[i]==nums[i-1]: continue #[1]
            
            while j<k:
                s = nums[i]+nums[j]+nums[k]
                
                if s>0:
                    k -= 1
                elif s<0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    
                    while j<k and nums[k]==nums[k-1]: k -= 1 #[2]
                    while j<k and nums[j]==nums[j+1]: j += 1 #[3]
                    k -= 1
                    j += 1
                    
        return ans
