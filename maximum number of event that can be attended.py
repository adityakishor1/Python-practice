class Solution(object):
    def maxEvents(self, A):
        d = 0
        count = 0
        h = [] #a heap. store the started event
        A.sort(reverse=True)
        
        #for each day, attend the event with smallest endtime, so we can have the most free time in the future.
        while A or h:
            if not h: d = A[-1][0]
            
            while A and A[-1][0]<=d:
                heapq.heappush(h, A.pop()[1])
            
            heapq.heappop(h) #attend the event with smallest endtime
            count += 1
            d += 1
            
            while h and h[0]<d: heapq.heappop(h) #remove the ended event
        
        return count
