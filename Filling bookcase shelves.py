class Solution(object):
    def minHeightShelves(self, books, W):
        dp = [float('inf')]*len(books)
        
        dp[0] = books[0][1]
        
        for i in xrange(1, len(books)):
            topLevelWidth = 0
            topLevelMaxHeight = 0
            
            for j in xrange(i, -1, -1):
                topLevelWidth += books[j][0]
                topLevelMaxHeight = max(topLevelMaxHeight, books[j][1])
                if topLevelWidth>W: break
                dp[i] = min(dp[i], (dp[j-1] if j-1>=0 else 0) + topLevelMaxHeight)
                
        return dp[-1]
                
