from collections import deque

class Solution:
    def zigZagTraversal(self, root):
        if not root:
            return []

        result = []
        queue = deque()
        queue.append(root)
        left_to_right = True

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not left_to_right:
                level_nodes.reverse()

            result.extend(level_nodes)
            left_to_right = not left_to_right  

        return result
