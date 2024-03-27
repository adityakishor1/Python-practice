class Solution(object):
    def maximumSum(self, arr):
        if not arr: return arr
        if len(arr)==1: return arr[0]
        
        dp = [[0, 0] for _ in xrange(len(arr))]
        subarrayMaxSum = arr[0]
        
        for i in xrange(len(arr)):
            if i==0:
                dp[i][0] = arr[i]
                dp[i][1] = arr[i]
            else:
                dp[i][0] = max(dp[i-1][0]+arr[i], arr[i])
                dp[i][1] = max(dp[i-1][0], dp[i-1][1]+arr[i])
            subarrayMaxSum = max(subarrayMaxSum, dp[i][0], dp[i][1])
        
        return subarrayMaxSum
