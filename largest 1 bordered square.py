class Solution(object):
    def largest1BorderedSquare(self, grid):
        if not grid or not grid[0]: return 
        M, N = len(grid), len(grid[0])
        
        dp = [[[0, 0] for _ in xrange(N+1)] for _ in xrange(M+1)]
        ans = 0
        for i in xrange(M):
            for j in xrange(N):
                if grid[i][j]==1:
                    #[0]
                    dp[i+1][j+1][0] = dp[i][j+1][0]+1
                    dp[i+1][j+1][1] = dp[i+1][j][1]+1

                    #[1]
                    K = min(dp[i+1][j+1][0], dp[i+1][j+1][1])
                    
                    #[2]
                    for k in xrange(K, -1, -1):
                        if dp[i+1-k+1][j+1][1]>=k and dp[i+1][j+1-k+1][0]>=k:
                            ans = max(ans, k**2)
                            break
                    
                elif grid[i][j]==0:
                    #[0]
                    dp[i+1][j+1][0] = 0
                    dp[i+1][j+1][1] = 0

        return ans
