class Solution(object):
    def maximalSquare(self, matrix):
        """
        dp[i][j] := maximal square length with matrix[i-1][j-1] at the bottom right corner in the square
        """
        ans = 0
        N = len(matrix)
        M = len(matrix[0])
        
        dp = [[0 for _ in xrange(M+1)] for _ in xrange(N+1)]
        
        for i in xrange(1, N+1):
            for j in xrange(1, M+1):
                if matrix[i-1][j-1]=='1':
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1
                    ans = max(ans, dp[i][j]**2)
        return ans
