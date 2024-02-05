class Solution(object):
    def characterReplacement(self, s, k):
        counter = collections.Counter()
        ans = 0
        
        l = 0
        for r in xrange(len(s)):
            counter[s[r]] += 1
            
            while r-l+1-max(counter.values())>k:
                counter[s[l]] -= 1
                l += 1
                
            ans = max(ans, r-l+1)
        return ans
