class Solution(object):
    def backspaceCompare(self, s, t):
        def helper(S):
            ans = ''
            i = len(S)-1
            backspaceCount = 0
            
            while i>=0:
                if S[i]=='#':
                    backspaceCount += 1
                else:
                    if backspaceCount>0:
                        backspaceCount -= 1
                    else:
                        ans += S[i]
                i -= 1
            return ans
        
        return helper(s)==helper(t)
