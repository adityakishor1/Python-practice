class Solution(object):
    def shipWithinDays(self, weights, D):
        l = max(weights)
        r = sum(weights)
        
        while l<r:
            c = (l+r)/2
            d = 0
            daily_weight = 0
            for w in weights:
                if daily_weight+w<=c:
                    daily_weight+=w
                else:
                    daily_weight = w
                    d += 1
            if daily_weight: d += 1

            if d>D:
                l = c+1
            else:
