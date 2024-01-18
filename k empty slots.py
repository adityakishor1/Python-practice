from sortedcontainers import SortedSet

class Solution(object):
    def kEmptySlots(self, schedule, K):
        def check(l, r):
            if l<0 or r>=len(bulbs): return False
            if bulbs[l]!=1 or bulbs[r]!=1: return False
            
            i = ss.bisect_right(l)
            j = ss.bisect_left(r)
            
            return j!=0 and i!=len(ss) and i==j
        
        bulbs = [0]*len(schedule)
        ss = SortedSet()
        for day, x in enumerate(schedule):
            i = x-1
            bulbs[i] = 1
            ss.add(i)
            if check(i, i+K+1): return day+1
            if check(i-(K+1), i): return day+1
        return -1
