class Solution(object):
    def inorderTraversal(self, root):
        def helper(node):
            if not node: return
            helper(node.left)
            opt.append(node.val)
            helper(node.right)
            
        opt = []
        helper(root)
        return opt
        
