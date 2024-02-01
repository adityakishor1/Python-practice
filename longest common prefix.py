class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs)==0 or strs==None:
            return ''
        
        bench_mark = strs[0] #[0]
        
        for i in range(1, len(bench_mark)+1): #[1]
            common_substring = bench_mark[:i]
            for s in strs:
                if s[:i]!=common_substring: #[2]
                    return bench_mark[:i-1]
        return bench_mark #[3]
