class Solution(object):
    def buildTree(self, preorder, inorder):
        def helper(i, j, k, l):
            root = TreeNode(preorder[i])
            
            r = inorderIndex[root.val] #the index of the root val in inorder
            leftLength = r-k
            rightLength = l-(r+1)
            
            if leftLength>0: root.left = helper(i+1, i+1+leftLength, k, k+leftLength)
            if rightLength>0: root.right = helper(i+1+leftLength, i+1+leftLength+rightLength, r+1, r+1+rightLength)
            return root
        
        inorderIndex = {}
        for i, n in enumerate(inorder): inorderIndex[n] = i
        return helper(0, len(preorder), 0, len(inorder))
