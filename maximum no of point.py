class Solution(object):
    def maxPoints(self, points):
        N = len(points)
        M = len(points[0])
        dp = [[0]*M for _ in xrange(N)]

        for j in xrange(M):
            dp[0][j] = points[0][j]
        
        for i in xrange(1, N):
            rollingMax = float('-inf')
            for j in xrange(M):
                rollingMax = max(rollingMax, dp[i-1][j] - j)
                dp[i][j] = max(dp[i][j], points[i][j] + j + rollingMax))
            
            rollingMax = float('-inf')
            for j in xrange(M, -1, -1):
                rollingMax = max(rollingMax, dp[i-1][j] + j)
                dp[i][j] = max(dp[i][j], points[i][j] - j + rollingMax))

        return max(dp[N-1])
