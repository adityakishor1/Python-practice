class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        node = root
        
        while node:
            if node.val>q.val and node.val>p.val:
                node = node.left
            elif node.val<q.val and node.val<p.val:
                node = node.right
            else:
                return node
