class Solution(object):
    def longestPalindrome(self, s):
        def findPalindorome(mid, mid2=None):
            r = 0
            l = len(s)
            max_pal = ''

            if mid2:
                #case 2
                if mid<0 or mid>=l: return ''
                if mid2<0 or mid2>=l: return ''
                while mid-r>=0 and mid2+r<l and s[mid-r]==s[mid2+r]:
                    max_pal = s[mid-r:mid2+r+1]
                    r+=1
            else:
                #case 1
                if mid<0 or mid>=l: return ''
                while mid-r>=0 and mid+r<l and s[mid-r]==s[mid+r]:
                    max_pal = s[mid-r:mid+r+1]
                    r+=1
            return max_pal
                
        max_pal = ''
        l = len(s)
        for i in range(len(s)):
            #case 1
            p = findPalindorome(i)
            max_pal = p if len(p)>len(max_pal) else max_pal

            #case 2
            p2 = findPalindorome(i, i+1)
            max_pal = p2 if len(p2)>len(max_pal) else max_pal
            
        return max_pal
