class Solution(object):
    def hIndex(self, citations):
        N = len(citations)
        
        l = 0
        r = N-1
        
        while l<r:
            i = (l+r)/2
            h = N-i

            if citations[i]>=h:
                #h may be the h-index, check larger h.
                r = i
            else:
                #h is not h-index, check smaller h.
                l = i+1
        
        #now, l is equal to r

        return N-l if citations[l]!=0 else 0 
