class Solution(object):
    def balanceBST(self, root):
        def getInorderNodes(root):
            nodes = []
            stack = []
            node = root
            
            while node or stack:
                while node:
                    stack.append(node)
                    node = node.left
                
                node = stack.pop()
                nodes.append(node)
                node = node.right
            
            return nodes
                
        def getRoot(l, r):
            if l>r: return None
            m = (l+r)/2
            root = inorderNodes[m]
            root.left = getRoot(l, m-1)
            root.right = getRoot(m+1, r)
            return root
            
        inorderNodes = getInorderNodes(root)
        return getRoot(0, len(inorderNodes)-1)
