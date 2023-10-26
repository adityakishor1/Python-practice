class Solution(object):
    def isBalanced(self, root):

        def helper(node, depth):
            if not node.left and not node.right: return depth
            
            l = r = depth #l: left_max_depth, r: right_max_depth
            if node.left:
                l = helper(node.left, depth+1)
            if node.right:
                r = helper(node.right, depth+1)

            if l!=-1 and r!=-1 and abs(l-r)<=1:
                return max(l, r)
            return -1
        
        if not root: return Tr
