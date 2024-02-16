class Solution(object):
    def majorityElement(self, nums):
        ans = nums[0]
        count = 0
        
        for n in nums:
            if n==ans:
                count += 1
            else:
                count -= 1
                if count==0:
                    ans = n
                    count = 1
        return ans
                
