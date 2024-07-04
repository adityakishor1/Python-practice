class Solution(object):
    def nthUglyNumber(self, k):
        i2 = i3 = i5 = 0
        
        ans = [1]
        while len(ans)<k:
            n2 = ans[i2]*2
            n3 = ans[i3]*3
            n5 = ans[i5]*5
            
            n = min(n2, n3, n5)
            ans.append(n)
            
            if n2==n: i2 += 1
            if n3==n: i3 += 1
            if n5==n: i5 += 1
                
        return ans[-1]
