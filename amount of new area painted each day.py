class Solution(object):
    def amountPainted(self, paint):
        ans = [0]*len(paint)
        box = SortedList()
        records = []
        maxPos = float('-inf')
        
        #[1]
        for i, (start, end) in enumerate(paint):
            records.append((start, i, -1))
            records.append((end, i, 1))
            maxPos = max(maxPos, end)
        
        records.sort()
        
        #[2]
        i = 0
        for pos in xrange(maxPos+1):
            while i<len(records) and records[i][0]==pos:
                _, index, t = records[i]
                if t==-1:
                    box.add(index)
                else:
                    box.remove(index)
                i += 1
            
            if box: ans[box[0]] += 1 #[3]
        return ans
