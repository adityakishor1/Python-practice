class Solution(object):
    def longestStrChain(self, words):
        def isPredecessor(word, word2):
            if not word or not word2: return False
            for i in xrange(len(word)):
                if word[:i]+word[i+1:]==word2:
                    return True
            return False

        def shortestPredecessor(word):
            if word in history: return history[word]
            shortest_predecessor = word
            for word2 in word_group[len(word)-1]:
                if isPredecessor(word, word2):
                    sp = shortestPredecessor(word2)
                    if len(sp)<len(shortest_predecessor): shortest_predecessor = sp
            history[word] = shortest_predecessor
            return history[word]

        word_group = collections.defaultdict(list)
        ans = 1
        history = {} # classic memorization for the recursion.
        
        for word in words:
            word_group[len(word)].append(word)
        
        for l in xrange(max(word_group.keys()), 0, -1):
            if l<ans: break # no need to check since the l is already too small
            for word in word_group[l]:
                ans = max(ans, l-len(shortestPredecessor(word))+1)
        
        return ans
