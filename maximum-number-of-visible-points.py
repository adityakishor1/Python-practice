class Solution(object):
    def visiblePoints(self, points, angle, location):
        def getAngle(x, y):
            #4 axis
            if x>0 and y==0:
                return 0
            elif x==0 and y>0:
                return 90
            elif x<0 and y==0:
                return 180
            elif x==0 and y<0:
                return 270
            
            #4 quadrant
            if x>0 and y>0:
                return math.degrees(math.atan2(abs(y), abs(x)))
            elif x<0 and y>0:
                return 180-math.degrees(math.atan2(abs(y), abs(x)))
            elif x<0 and y<0:
                return 180+math.degrees(math.atan2(abs(y), abs(x)))
            else:
                return 360-math.degrees(math.atan2(abs(y), abs(x)))
            
        ans = 0
        onLocation = 0
        angles = []
        
        for x, y in points:
            if x==location[0] and y==location[1]:
                onLocation += 1
            else:
                a = getAngle(x-location[0], y-location[1])
                angles.append(a)
                if a<=angle: angles.append(360+a) #[1]
        
        angles.sort()
        
        i = 0
        for j in xrange(len(angles)):
            while angles[j]-angles[i]>angle:
                i += 1
            ans = max(ans, j-i+1)
                
        return ans+onLocation
