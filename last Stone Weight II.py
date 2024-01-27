class Solution(object):
    def lastStoneWeightII(self, stones):
        total = sum(stones)
        target = total/2
        dp = [[False for _ in xrange(target+1)] for _ in xrange(len(stones)+1)]
        dp[0][0] = True
        
        maxSum = 0
        # Keep trace of the max sum that stones can sum up to.
        
        for i in xrange(1, len(stones)+1):
            for t in xrange(target+1):
                if (dp[i-1][t] or (t-stones[i-1]>=0 and dp[i-1][t-stones[i-1]])):
                   
                    dp[i][t] = True
                    maxSum = max(maxSum, t)
                    if t==target: return total-maxSum*2
        
        return total-maxSum*2

