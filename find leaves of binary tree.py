class Solution(object):
    def findLeaves(self, root):
        ans = []
        q = collections.deque([root])
        parents = {}
        
        #[1]
        temp = []
        while q:
            node = q.popleft()
            
            if not node.left and not node.right:
                temp.append(node)
            
            if node.left:
                q.append(node.left)
                parents[node.left] = node
            
            if node.right:
                q.append(node.right)
                parents[node.right] = node

        #[2] 
        while temp:
            ans.append(temp)
            temp = []
            
            for node in ans[-1]:
                if node not in parents: break
                p = parents[node]
                if p.left==node: p.left = None
                if p.right==node: p.right = None
                if not p.left and not p.right: temp.append(p)
        
        #[3]
        ans2 = []
        for temp in ans:
            ans2.append([node.val for node in temp])
        
        return ans2
