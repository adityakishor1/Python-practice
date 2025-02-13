class Solution:
    def findTarget(self, root, target):
        if not root:
            return False

        # Helper function to perform in-order traversal using a stack
        def next_inorder(stack):
            while stack:
                node = stack.pop()
                x = node
                right = node.right
                while right:
                    stack.append(right)
                    right = right.left
                return x.data
            return None
        def next_reverse_inorder(stack):
            while stack:
                node = stack.pop()
                x = node
                left = node.left
                while left:
                    stack.append(left)
                    left = left.right
                return x.data
            return None
        inorder_stack, reverse_stack = [], []
        node = root
        while node:
            inorder_stack.append(node)
            node = node.left  
        
        node = root
        while node:
            reverse_stack.append(node)
            node = node.right  
        left_val = next_inorder(inorder_stack)
        right_val = next_reverse_inorder(reverse_stack)
        while left_val is not None and right_val is not None and left_val < right_val:
            curr_sum = left_val + right_val
            if curr_sum == target:
                return True
            elif curr_sum < target:
                left_val = next_inorder(inorder_stack)
            else:
                right_val = next_reverse_inorder(reverse_stack)

        return False
