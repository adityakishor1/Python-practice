class Solution(object):
    def rob(self, root):
        def get_max_value(node):
            if node is None: return 0, 0
            left_rob, left_not_rob = get_max_value(node.left)
            right_rob, right_not_rob = get_max_value(node.right)

            rob = node.val+left_not_rob+right_not_rob
            not_rob = max(left_rob, left_not_rob)+max(right_rob, right_not_rob)

            return rob, not_rob

        return max(get_max_value(root))
