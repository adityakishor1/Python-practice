class Solution(object):
    def wiggleMaxLength(self, nums):
        N = len(nums)
        
        ans = 1
        up = 1
        down = 1
        
        for i in xrange(2, N+1):
            if nums[i-1]-nums[i-2]>0:
                up, down = down+1, down
            elif nums[i-1]-nums[i-2]<0:
                down = up+1
                
            ans = max(ans, up, down)

        return ans
