class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        ans = ''
        
        replacement = {}
        for i in xrange(len(indices)):
            index = indices[i]
            source = sources[i]
            target = targets[i]
            
            if s[index:index+len(source)]!=source: continue
            replacement[index] = (source, target)
        
        i = 0
        while i<len(s):
            if i not in replacement:
                ans += s[i]
                i += 1
            else:
                ans += replacement[i][1]
                i += len(replacement[i][0])
        
        return ans
