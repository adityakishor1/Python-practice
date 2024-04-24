class Solution(object):
    def getMinimumDifference(self, root):
        def traverse(node):
            if not node: return
            traverse(node.left)
            A.append(node.val)
            traverse(node.right)
            
        A = []
        ans = float('inf')
        traverse(root)
        
        for i, n in enumerate(A):
            if i==0: continue
            ans = min(ans, A[i]-A[i-1])
        return ans
