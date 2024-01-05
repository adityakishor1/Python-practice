import collections

class Solution(object):
    def hIndex(self, citations):
        counter = collections.Counter() #count for each citation
        N = len(citations)
        count = 0
        
        for citation in citations:
            counter[min(N, citation)] += 1 #[0]
            
        for n in xrange(N, -1, -1):
            count += counter[n] #count of citation that is larger or equal to n
            if count>=n: return n
        
        return 0
