class Solution(object):
    def combinationSum3(self, k, n):
        def helper(remain, comb, k, start):
            if remain==0 and len(comb)==k:
                ans.append(comb[:])
            elif remain<0 or len(comb)>k:
                return
            else:
                for i in xrange(start, len(nums)):
                    used = nums[i]
                    num = i+1
                    
                    if used: continue
                        
                    comb.append(num)
                    nums[i] = True
                    
                    helper(remain-num, comb, k, i+1)
                    
                    comb.pop()
                    nums[i] = False
        
        nums = [False]*9
        ans = []
        helper(n, [], k, 0)
        return ans
