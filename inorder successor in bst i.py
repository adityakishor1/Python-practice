class Solution(object):
    def inorderSuccessor(self, root, p):
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        else:
            stack = []
            node = root
            prev = None
            while node or stack:
                while node:
                    stack.append(node)
                    node = node.left
                
                node = stack.pop()
                
                if prev==p: return node

                prev = node
                node = node.right
            return None
