class Solution:
    def getMaxSum(self, root):
        
        def helper(node):
            if not node:
                return (0, 0)
            
            left = helper(node.left)
            right = helper(node.right)
            include = node.data + left[1] + right[1]
            exclude = max(left) + max(right)
            
            return (include, exclude)
        
        result = helper(root)
        return max(result)
