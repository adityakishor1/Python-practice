class Solution(object):
    def deleteNode(self, root, key):
        def find_min(root):
            curr = root
            while curr.left: curr = curr.left
            return curr.val#[5]
        
        def remove(node):
            if node.left and node.right:
                node.val = find_min(node.right)
                node.right = self.deleteNode(node.right, node.val)
                return node #[4]
            elif node.left and not node.right:
                return node.left #[3]
            elif node.right and not node.left:
                return node.right #[3]
            else:
                return None #[2]
            
        if not root: return root
        node = root
        
        while node: #[0]
            if node.val==key:
                return remove(node) #[1]
            elif node.left and node.left.val==key:
                node.left = remove(node.left) #[1]
                return root
            elif node.right and node.right.val==key:
                node.right = remove(node.right) #[1]
                return root
            
            if key>node.val and node.right:
                node = node.right
            elif key<node.val and node.left:
                node = node.left
            else:
                break
                
        return root
