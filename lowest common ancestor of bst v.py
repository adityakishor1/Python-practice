class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        stack = []
        stack.append(root)

        parent = {}
        parent[root] = None

        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        
        p_ancestor = p
        q_ancestor = q
        p_ancestors = set()
        while p_ancestor:
            p_ancestors.add(p_ancestor)
            p_ancestor = parent[p]
        while q_ancestor:
            if q_ancestor in p_ancestors: return q_ancestor
            q_ancestor = parent[q]
            
        return None

