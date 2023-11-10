class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        bucket = {}
        
        for i, num in enumerate(nums):
            if len(bucket)>k:
                bidToRemove = nums[i-k-1]//(t+1)
                del bucket[bidToRemove]
            
            bid = num//(t+1)
            if bid in bucket: return True
            if bid+1 in bucket and abs(bucket[bid+1]-num)<=t: return True
            if bid-1 in bucket and abs(bucket[bid-1]-num)<=t: return True
            bucket[bid] = num
        
        return False
