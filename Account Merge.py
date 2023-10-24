class Solution(object):
    def accountsMerge(self, accounts):
        
        #build adjacency list
        adj = collections.defaultdict(list)
        for account in accounts:
            name = account[0]
            email0 = account[1]
            for i in xrange(2, len(account)):
                email = account[i]
                adj[email0].append(email)
                adj[email].append(email0)
        
        #iterate accounts and dfs each email group
        ans = []
        visited = set() #store all the visited email
        for account in accounts:
            name = account[0]
            email0 = account[1]
            if email0 in visited: continue
            
            #dfs
            group = set() #store the email group related to email0
            stack = [email0]
            while stack:
                email = stack.pop()
                if email in group or email in visited: continue
                group.add(email)
                visited.add(email)
                for nei in adj[email]:
                    stack.append(nei)
            
            ans.append([name]+sorted(list(group)))
        
        return ans
            
