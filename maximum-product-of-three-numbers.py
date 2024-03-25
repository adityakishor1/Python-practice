class Solution(object):
    def maximumProduct(self, nums):
        min1 = float('inf') #smallest
        min2 = float('inf') #second smallest

        max1 = float('-inf') #largest
        max2 = float('-inf') #second largest
        max3 = float('-inf') #third largest

        for n in nums:
            if n<=min1:
                min2 = min1
                min1 = n
            elif n<=min2:
                min2 = n
            
            if n>=max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n>=max2:
                max3 = max2
                max2 = n
            elif n>=max3:
                max3 = n

        return max(min1*min2*max1, max1*max2*max3)
