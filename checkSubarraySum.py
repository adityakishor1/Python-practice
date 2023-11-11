class Solution(object):
    def checkSubarraySum(self, nums, k):
        prefixSumEndings = collections.defaultdict(list)
        prefixSumEndings[0].append(-1)
        
        prefixSum = 0
        for i, n in enumerate(nums):
            prefixSum += n
            
            x = prefixSum/k
            while x>=0:
                p2 = prefixSum-k*x
                if len(prefixSumEndings[p2])>0 and prefixSumEndings[p2][0]<i-1:
                    return True
                x -= 1
            prefixSumEndings[prefixSum].append(i)
        
        return False
