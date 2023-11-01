class Solution(object):
    def maxCoins(self, nums):
        N = len(nums)
        
        dp = [[0 for _ in xrange(N)] for _ in xrange(N)]
        for i in xrange(N): dp[i][i] = (nums[i-1] if 0<=i-1 else 1) * nums[i] * (nums[i+1] if i+1<N else 1)
            
        for l in xrange(2, N+1):
            for i in xrange(N):
                j = i+l-1
                if j>=N: continue
                for k in xrange(i, j+1):
                    dp[i][j] = max(dp[i][j],
                        (dp[i][k-1] if k-1>=0 else 0) +
                        (nums[i-1] if 0<=i-1 else 1) * nums[k] * (nums[j+1] if j+1<N else 1) +
                        (dp[k+1][j] if k+1<N else 0)
                    )
        
        return dp[0][N-1]
