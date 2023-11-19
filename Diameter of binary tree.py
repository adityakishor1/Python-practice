class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        
        def traverse(node):
            if not node: return 0
            left, right = traverse(node.left), traverse(node.right)
            self.diameter = max(self.diameter, left+right)
            return max(left, right)+1
        
        #iterate through the tree
        traverse(root)
        return self.diameter
