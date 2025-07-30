class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for word in strs[1:]:
                if i >= len(word) or word[i] != strs[0][i]:
                    return strs[0][:1]
        return strs[0]
