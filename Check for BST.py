class Solution:
    def isBSTUtil(self, node, min_val, max_val):
        if not node:
            return True
        
        if node.data <= min_val or node.data >= max_val:
            return False
        
        return (self.isBSTUtil(node.left, min_val, node.data) and
                self.isBSTUtil(node.right, node.data, max_val))
    def isBST(self, root):
        return self.isBSTUtil(root, float('-inf'), float('inf'))
