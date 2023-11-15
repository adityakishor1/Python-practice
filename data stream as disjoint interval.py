class SummaryRanges(object):

    def __init__(self):
        self.nums = []
        

    def addNum(self, val):
        bisect.insort_left(self.nums, val)
        

    def getIntervals(self):
        ans = []
        
        for num in self.nums:
            if not ans:
                ans.append([num, num])
            elif ans[len(ans)-1][1]+1==num:
                ans[len(ans)-1][1] = num
            elif ans[len(ans)-1][1]<num:
                ans.append([num, num])
        return ans
