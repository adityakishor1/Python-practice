class Solution(object):
    def minCostClimbingStairs(self, cost):
        def helper(i):
            if i in history: return history[i]
            
            if i>len(cost)-1:
                history[i] = 0
            elif i==len(cost)-1 or i==len(cost)-2:
                history[i] = cost[i]
            elif i<len(cost)-2:
                history[i] = cost[i] + min(helper(i+1), helper(i+2))
                
            return history[i]
        
        history = {}
        return min(helper(0), helper(1))
            
