class Solution(object):
    def binaryTreePaths(self, root):
        q = collections.deque([(root, '')])
        ans = []
        
        while q:
            node, path = q.popleft()
            
            path = (path+'->'+str(node.val)) if path else str(node.val)
            
            if node.left: q.append((node.left, path))
            if node.right: q.append((node.right, path))

            if not node.left and not node.right: ans.append(path)
            
        return ans
