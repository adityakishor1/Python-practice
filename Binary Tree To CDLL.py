def bTreeToClist(self, root):
        head, tail = self.construct_dll(root)
        if head:
            tail.right = head
            head.left = tail
        return head
    
def construct_dll(self, root):
        head = None
        tail = None
        
        if not root:
            return head, tail
        
        l_head , l_tail = self.construct_dll(root.left)
        root_node = root
        r_head, r_tail = self.construct_dll(root.right)
        
        if not l_head:
            head = root_node
            tail = root_node
            
        if l_head:
            l_tail.right = root_node
            root_node.left = l_tail
            head = l_head
            tail = root_node
        
        if r_head:
            tail.right = r_head
            r_head.left = tail
            tail = r_tail
        
        return head, tail
