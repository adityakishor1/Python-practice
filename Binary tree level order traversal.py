class Solution(object):
    def levelOrderBottom(self, root):
        if not root: return []
        ans = []
        q = collections.deque([root])
        
        while q:
            ans.append([])
            currLevelCount = len(q)
            for _ in xrange(currLevelCount):
                node = q.popleft()
                ans[-1].append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return reversed(ans)
