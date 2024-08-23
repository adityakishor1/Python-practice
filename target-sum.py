class Solution(object):
    def findTargetSumWays(self, nums, S):
        stack = [(0, 0)]
        ans = 0
        
        while stack:
            i, s = stack.pop()
            if i==len(nums) and s==S: ans += 1
            if i>=len(nums): continue
            
            stack.append((i+1, s+nums[i]))
            stack.append((i+1, s-nums[i]))
        
        return ans
