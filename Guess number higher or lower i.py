class Solution(object):
    def guessNumber(self, n):
        l = 1
        h = n
        
        while l<h:
            m = (l+h)/2    
            
            r = guess(m)
            
            if r==0:
                return m
            elif r==1:
                l = m+1
            elif r==-1:
                h = m-1
                
        return (l+h)/2
