class Solution:
    def multiplyStrings(self, s1, s2):
        s1 = s1.lstrip('0')
        s2 = s2.lstrip('0')
        if not s1 or not s2:
            return "0"
        neg = False
        if s1[0] == '-':
            neg = not neg
            s1 = s1[1:]
        if s2[0] == '-':
            neg = not neg
            s2 = s2[1:]
        
        n, m = len(s1), len(s2)
        res = [0] * (n + m)
        s1 = s1[::-1]
        s2 = s2[::-1]
        
        for i in range(n):
            for j in range(m):
                res[i+j] += (ord(s1[i]) - ord('0')) * (ord(s2[j]) - ord('0'))
                res[i+j+1] += res[i+j] // 10
                res[i+j] = res[i+j] % 10
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        
        ans = ''.join(map(str, res[::-1]))
        
        if neg:
            ans = '-' + ans
        return ans
