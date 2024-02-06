class Solution(object):
    def longestSubstring(self, s, k):
        def helper(l, r):
            if r-l==0: return 0
            counter = collections.Counter(s[l:r])
            
            i = l
            while i<r:
                c = s[i]
                
                if counter[c]>=k:
                    i += 1
                else:
                    return max(helper(l, i), helper(i+1, r))
            return i-l
        
        return helper(0, len(s))
