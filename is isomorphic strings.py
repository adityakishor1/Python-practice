class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)!=len(t): return False
        
        # check if s1 chars could be replaced and become s2
        def helper(s1, s2):
            memo = {}
            
            for i in xrange(len(s)):
                c1 = s1[i]
                c2 = s2[i]
                
                if c1 in memo and memo[c1]!=c2: return False
                memo[c1] = c2
            return True
        
        return helper(s, t) and helper(t, s)
