class Solution(object):
    def longestUnivaluePath(self, root):
        def getUnivalueLength(node, val):
            if not node: return 0
            
            l, r = getUnivalueLength(node.left, node.val), getUnivalueLength(node.right, node.val)
            self.ans = max(self.ans, l+r)
            
            if node.val==val: return 1+max(l, r)
            return 0
            
        if not root: return 0
        self.ans = float('-inf')
        getUnivalueLength(root, root.val)
        return self.ans
