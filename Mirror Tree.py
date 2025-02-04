class Solution:
    def mirror(self, root):
        if root is None:
            return
        root.left, root.right = root.right, root.left
        
        # Recursively mirror left and right subtrees
        self.mirror(root.left)
        self.mirror(root.right)
