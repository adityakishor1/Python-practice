class Solution(object):
    def knightProbability(self, N, K, r, c):
        if K==0: return 1
        
        dp = [[[0 for _ in xrange(N)] for _ in xrange(N)] for _ in xrange(K+1)]
        
        dp[0][r][c] = 1
        possible = float(0)
        
        for k in xrange(1, K+1):
            for i in xrange(N):
                for j in xrange(N):
                    if dp[k-1][i][j]>0:
                        for x, y in [(i+1, j+2), (i-1, j+2), (i+1, j-2), (i-1, j-2), (i+2, j+1), (i-2, j+1), (i+2, j-1), (i-2, j-1)]:
                            if 0<=x and x<N and 0<=y and y<N:
                                dp[k][x][y]+=dp[k-1][i][j]
                                if k==K: possible+=dp[k-1][i][j] #calculate the possible in the last iteration.
                                
        return possible/(8**K)
