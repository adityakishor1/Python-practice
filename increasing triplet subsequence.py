class Solution(object):
    def increasingTriplet(self, nums):
        min1 = min2 = float('inf')
        
        for n in nums:
            if n<min1:
                min1 = n
            elif min1<n and n<min2:
                min2 = n
            elif min2<n:
                return True
        
        return False
