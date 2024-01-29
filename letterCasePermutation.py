class Solution(object):
    def letterCasePermutation(self, S):
        def dfs(path, i):
            if i>=len(S):
                opt.append(path)
                return
            if S[i] not in num_char:
                dfs(path+S[i].upper(), i+1)
                dfs(path+S[i].lower(), i+1)
            else:
                dfs(path+S[i], i+1)

        num_char = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        opt = []
        dfs('', 0)
        return opt
