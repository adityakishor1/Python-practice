lass Solution(object):
    def findSecretWord(self, wordlist, master):
        def similarity(w1, w2):
            count = 0
            for i in xrange(6):
                if w1[i]==w2[i]: count += 1
            return count
        
        for _ in xrange(10):
            
            temp = []
            
            word = random.choice(wordlist)
            k = master.guess(word)
            if k==6: return
            
            for otherWord in wordlist:
                if otherWord==word: continue
                if similarity(word, otherWord)==k: temp.append(otherWord)
            
            wordlist = temp
