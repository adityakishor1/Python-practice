class Solution(object):
    def maxProfit(self, prices):
        if not prices or len(prices)<=1: return 0
        N = len(prices)

        buy = [-prices[0], max(-prices[1], -prices[0])]
        sell = [0, max(prices[1]+buy[0], 0)]
        
        for i in xrange(2, N):
            buy.append(max(sell[i-2]-prices[i], buy[i-1]))
            sell.append(max(prices[i]+buy[i-1], sell[i-1]))
            
        return max(buy[-1], sell[-1], 0)
