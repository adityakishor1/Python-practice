import heapq

class Solution:
    def getMedian(self, arr):
        low = []  
        high = []  
        medians = []
        
        for num in arr:
            if not low or num <= -low[0]:
                heapq.heappush(low, -num)  
            else:
                heapq.heappush(high, num)
            if len(low) > len(high) + 1:
                heapq.heappush(high, -heapq.heappop(low))
            elif len(high) > len(low):
                heapq.heappush(low, -heapq.heappop(high))
            
            if len(low) > len(high):
                medians.append(float(-low[0]))
            else:
                medians.append((-low[0] + high[0]) / 2.0)
        
        return medians
