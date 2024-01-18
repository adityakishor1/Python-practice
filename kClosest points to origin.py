class Solution(object):
    def kClosest(self, points, K):
        #[1]
        maxD = float('-inf')
        minD = float('inf')
        distances = []
        for x, y in points:
            distance = ((x**2+y**2)**0.5)
            distances.append((distance, x, y))
            maxD = max(maxD, distance)
            minD = min(minD, distance)
        
        #[2]
        ans = []
        smaller = []
        larger = []
        while K>0:
            #split distances into smaller and larger
            distance = (maxD+minD)/2
            for d, x, y in distances:
                if d<=distance:
                    smaller.append((d, x, y))
                else:
                    larger.append((d, x, y))
            
            if len(smaller)<=K:
                ans += smaller
                K -= len(smaller)
                distances = larger
                minD = distance
                larger = []
                smaller = []
            else:
                distances = smaller
                maxD = distance
                larger = []
                smaller = []
        
        return [(x, y) for _, x, y in ans]
