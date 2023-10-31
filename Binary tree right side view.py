class Solution(object):
    def rightSideView(self, root):
        if not root: return []
        
        ans = []
        currLevel = -1
        stack = [(root, 0)]
        
        while stack:
            node, level = stack.pop()
            if level>currLevel:
                ans.append(node.val)
                currLevel = level
            if node.left: stack.append((node.left, level+1))
            if node.right: stack.append((node.right, level+1))
                
        return ans
