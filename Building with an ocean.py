class Solution(object):
    def findBuildings(self, heights):
        ans = []
        currMaxHeight = 0
        for i in xrange(len(heights)-1, -1, -1):
            h = heights[i]
            if h>currMaxHeight: ans.append(i)
            currMaxHeight = max(currMaxHeight, h)
        
        return reversed(ans)
