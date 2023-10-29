class Solution(object):
    def longestConsecutive(self, root):
        if not root: return 0
        ans = 1
        stack = [(root, 1)]
        
        while stack:
            node, count = stack.pop()
            ans = max(ans, count)
            
            if node.left:
                stack.append((node.left, count+1 if node.val+1==node.left.val else 1))
            if node.right:
                stack.append((node.right, count+1 if node.val+1==node.right.val else 1))
                
        return ans
