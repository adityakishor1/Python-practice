class Solution(object):
    def firstUniqChar(self, string):
        counter = Counter(string)

        for i in xrange(len(string)):
            char = string[i]
            if counter[char]==1: return i

        return -1
