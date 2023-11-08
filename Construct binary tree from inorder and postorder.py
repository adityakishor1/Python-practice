class Solution(object):
    def buildTree(self, inorder, postorder):
        def helper(i, j, k, l):
            if i>j or k>l: return None
            rootVal = postorder[l]
            root = TreeNode(rootVal)
            r = inorderIndex[rootVal]
            leftLength = r-i
            rightLength = j-r
            root.left = helper(i, r-1, k, k+leftLength-1)
            root.right = helper(r+1, j, k+leftLength, k+leftLength+rightLength-1)
            return root
            
        inorderIndex = {}
        for i, n in enumerate(inorder): inorderIndex[n] = i
        return helper(0, len(inorder)-1, 0, len(postorder)-1)
