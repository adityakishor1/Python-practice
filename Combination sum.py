class Solution(object):
    def combinationSum(self, candidates, T):
        def dfs(index, target, path):
            if target<0:
                return
            elif target==0:
                opt.append(path)
            else:
                for i in xrange(index, len(candidates)):
                    num = candidates[i]
                    dfs(i, target-num, path+[num])
        opt = []
        candidates.sort()
        dfs(0, T, [])
        return opt
