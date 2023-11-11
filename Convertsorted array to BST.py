class Solution(object):
    def sortedArrayToBST(self, nums):
        def helper(i, j):
            m = (i+j)/2
            node = TreeNode(nums[m])
            
            leftLength = m-i #number of nodes in the left subtree
            rightLength = j-(m+1) #number of nodes in the right subtree
            
            if leftLength>0: node.left = helper(i, m)
            if rightLength>0: node.right = helper(m+1, j)
            return node
        
        return helper(0, len(nums))
