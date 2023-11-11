class Solution(object):
    def treeToDoublyList(self, root):
        def helper(node):
            ll = rr = node
            if node.left:
                ll, lr = helper(node.left)
                node.left = lr
                lr.right = node
            
            if node.right:
                rl, rr = helper(node.right)
                node.right = rl
                rl.left = node
            
            return ll, rr
        
        if not root: return root
        left, right = helper(root)
        right.right = left
        left.left = right
        return left
