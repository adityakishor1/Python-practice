class Solution(object):
    def minEatingSpeed(self, piles, H):
        if not piles: return 0
        
        l = 1
        r = max(piles) #[0]
        
        while l<r:
            K = (l+r)/2 #[1]
            
            #time Koko needs to eat all bananas
            t = sum([-(-banana_count//K) for banana_count in piles]) #-(-a//b) means ceil(a/b)
            
            if t>H:
                l = K+1
            else:
                r = K

        return l #[2]
