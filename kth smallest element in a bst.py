class Solution(object):
    def kthSmallest(self, root, k):
        stack = []
        node = root
        
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            
            k -= 1
            if k==0: return node.val
            
            node = node.right
        return node.val
