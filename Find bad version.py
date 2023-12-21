class Solution(object):
    def firstBadVersion(self, n):
        if isBadVersion(1): return 1
        
        l = 2
        h = n
        
        while l<h:
            v = (l+h)/2
            r1 = isBadVersion(v)
            r2 = isBadVersion(v-1)
            
            if r1 and not r2:
                return v
            elif not r1 and not r2:
                l = v+1
            elif r1 and r2:
                h = v-1
                
        return (l+h)/2
