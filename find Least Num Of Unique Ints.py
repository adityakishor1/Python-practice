class Solution(object):
    def findLeastNumOfUniqueInts(self, nums, k):
        counter = collections.Counter(nums)
        h = []
        
        for num in counter:
            heapq.heappush(h, (counter[num], num))
            
        for _ in xrange(k):
            count, num = heapq.heappop(h)
            count -= 1
            if count>0: heapq.heappush(h, (count, num))
        
        return len(h)
