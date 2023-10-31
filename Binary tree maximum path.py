class Solution(object):
    def maxPathSum(self, root):
        def helper(node):
            left_a = left_na = right_a = right_na = float('-inf')

            if node.left:
                left_a, left_na = helper(node.left)
            if node.right:
                right_a, right_na = helper(node.right)

            a = max(node.val, node.val+left_a, node.val+right_a)
            na = max(left_na, right_na, node.val+left_a+right_a, a)
            return a, na

        return max(helper(root))
