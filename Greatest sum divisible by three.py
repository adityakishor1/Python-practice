class Solution(object):
    def videoStitching(self, clips, T):
        if T==0: return 0
        if not clips: return -1
        
        clips.sort()
        print clips
        
        if clips[0][0]!=0: return -1
        if clips[0][1]>=T: return 1
        
        count = 0
        i = 0
        rightMost = 0
        
        while i<len(clips):
            right = rightMost
            while i<len(clips) and clips[i][0]<=rightMost:
                right = max(right, clips[i][1])
                i += 1
            
            if rightMost==right: return -1 #rightMost cannot be update anymore
            
            rightMost = right
            count += 1
            if rightMost >= T: return count
            
        return -1
