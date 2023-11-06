class Solution(object):
    def combinationSum2(self, candidates, target):
        def helper(remain, comb, start):
            if remain==0:
                ans.append(comb[:])
            elif remain<0:
                return
            else:
                for i in xrange(start, len(candidates)):
                    if i>start and candidates[i]==candidates[i-1]: continue
                    candidate = candidates[i]
                    comb.append(candidate)
                    helper(remain-candidate, comb, i+1)
                    comb.pop()
        
        ans = []
        candidates.sort()
        helper(target, [], 0)
        return ans
        
