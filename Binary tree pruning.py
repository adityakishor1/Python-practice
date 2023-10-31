class Solution(object):
    def pruneTree(self, node):
        if not node: return None
        node.left = self.pruneTree(node.left)
        node.right = self.pruneTree(node.right)
        if not node.left and not node.right and node.val==0: return None
        return node
