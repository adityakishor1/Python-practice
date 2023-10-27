class Solution(object):
    def maxProfit(self, prices):
        if prices is None or len(prices)==0: return 0
        
        memo = [0]*len(prices)
        min_price = float('inf')
        
        for i in xrange(len(prices)):
            min_price = min(min_price, prices[i])
            if i==0: continue
            memo[i] = max(prices[i]-min_price, memo[i-1])
        return memo[-1]
