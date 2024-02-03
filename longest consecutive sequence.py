class Solution(object):
    def longestConsecutive(self, nums):
        s = set(nums)
        ans = 0
        
        for n in s:
            if n-1 not in s:
                c = 1
                curr = n
                
                while curr+1 in s:
                    curr = curr+1
                    c += 1

                ans = max(ans, c)
                
        return ans
