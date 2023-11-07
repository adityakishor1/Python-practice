class Solution(object):
    def combine(self, N, K):
        def dfs(comb, start, N, K):
            if len(comb)==K: ans.append(comb[:])
            
            for n in xrange(start, N+1):
                comb.append(n)
                dfs(comb, n+1, N, K)
                comb.pop()
        
        ans = []
        dfs([], 1, N, K)
        return ans
