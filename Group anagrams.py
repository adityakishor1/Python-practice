class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = collections.defaultdict(list)
        
        for s in strs:
            anagrams[self.getKey(s)].append(s)
        
        return anagrams.values()
    
    def getKey(self, s):
        key = ''
        counts = collections.Counter(s)
        for c in 'abcdefghijklmnopqrstuvwxyz':
            key += counts[c]*c
        return key
