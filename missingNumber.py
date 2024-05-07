class Solution(object):
    def missingNumber(self, nums):
        maxNum = max(nums)
        s = set(nums)
        
        for num in xrange(maxNum+1):
            if num not in s:
                return num
        
        return maxNum+1
