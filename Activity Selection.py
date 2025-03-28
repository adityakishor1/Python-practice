class Solution:
    def activitySelection(self, start, finish):
        activities = sorted(zip(start, finish), key=lambda x: x[1])
        
        count = 1  
        last_end_time = activities[0][1]  
        
        for i in range(1, len(activities)):
            if activities[i][0] > last_end_time:  
                count += 1
                last_end_time = activities[i][1]  
        
        return count
