class Solution(object):
    def mySqrt(self, x):
        l = 0
        r = x
        
        while l<=r:
            m = (l+r)/2
            m_sqr = m**2
            
            if m_sqr==x or (m_sqr<x and x<(m+1)**2):
                return m
            elif m_sqr<x:
                l = m+1
            else:
                r = m-1
