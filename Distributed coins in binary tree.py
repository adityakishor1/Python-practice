class Solution(object):
    def distributeCoins(self, root):
        def count_moves(node):
            if not node: return 0
            l, r = count_moves(node.left), count_moves(node.right)
            self.moves += abs(l)+abs(r)
            return node.val-1+l+r

        self.moves = 0
        count_moves(root)
        return self.moves
