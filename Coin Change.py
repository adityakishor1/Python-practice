import collections
class Solution(object):
    def coinChange(self, coins, amount):
        visited = set()
        
        coins.sort(reverse=True)
        q = collections.deque([(0, 0)])
        
        while q:
            current_amount, count = q.popleft()
            
            if current_amount==amount: return count
            if current_amount>amount: continue
            if current_amount in visited: continue
            visited.add(current_amount)
            
            for coin in coins:
                q.append((current_amount+coin, count+1))
        return -1
