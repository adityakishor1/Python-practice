class Solution(object):
    def minMeetingRooms(self, intervals):
        if not intervals: return 0
        ans = 1
        h = []
        
        intervals.sort()
        heapq.heappush(h, (intervals[0][1], intervals[0][0]))
        
        for i in xrange(1, len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]
            
            e0, s0 = h[0]
            
            if s>=e0: heapq.heappop(h)
            heapq.heappush(h, (e, s))
            ans = max(ans, len(h))
            
        return ans
