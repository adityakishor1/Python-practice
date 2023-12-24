class Solution(object):
    def flatten(self, root):
        if not root: return None
        
        preHead = TreeNode(0)
        curr = preHead
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
            
            node.right = None
            node.left = None
            curr.right = node
            curr = curr.right
            
        return preHead.right
