class Solution(object):
    def climbStairs(self, n):
        def helper(n):
            if n in history: return history[n]
            
            if n==0 or n==1:
                history[n] = 1
            elif n==2:
                return 2
            elif n>2:
                history[n] = helper(n-1) + helper(n-2)
            
            return history[n]
            
        history = {}
        return helper(n)
