import bisect
class Solution(object):
    def lastStoneWeight(self, stones):
        stones.sort()
        
        while len(stones)>1:
            x = stones.pop()
            y = stones.pop()
            bisect.insort_left(stones, abs(x-y))

        return 0 if not stones else stones[0]
