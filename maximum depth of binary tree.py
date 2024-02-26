class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        
        ans = float('-inf')
        q = collections.deque([(root, 1)])
        node = root
        
        while q:
            node, d = q.popleft()
            
            ans = max(ans, d)
            
            if node.left: q.append((node.left, d+1))
            if node.right: q.append((node.right, d+1))
        
        return ans
