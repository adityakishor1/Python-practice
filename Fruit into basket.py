class Solution(object):
    def totalFruit(self, fruits):
        ans = 0
        uniqueFruits = 0
        i = 0
        counter = collections.Counter()
        
        for j, fruit in enumerate(fruits):
            counter[fruit] += 1
            if counter[fruit]==1: uniqueFruits += 1
            
            while uniqueFruits>2:
                counter[fruits[i]] -= 1
                if counter[fruits[i]]==0: uniqueFruits -= 1
                i += 1
            
            ans = max(ans, j-i+1)
        return ans
