class Solution(object):
    def verticalOrder(self, root):
        if not root: return []
        ans = []
        minX = float('inf')
        maxX = float('-inf')
        locations = collections.defaultdict(list)
        q = collections.deque([(root, 0)])
        
        while q:
            node, x = q.popleft()
            locations[x].append(node.val)
            minX = min(minX, x)
            maxX = max(maxX, x)
            if node.left: q.append((node.left, x-1))
            if node.right: q.append((node.right, x+1))
        
        for x in xrange(minX, maxX+1):
            if locations[x]: ans.append(locations[x])
                
        return ans
