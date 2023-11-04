class Solution(object):
    def cloneGraph(self, node):
        if not node: return node
        
        visited = set()
        clones = {}
        stack = []
        
        stack.append(node)
        while stack:
            curr = stack.pop()
            if curr in visited: continue
            visited.add(curr)
            clones[curr] = Node(curr.val)
            stack.extend(curr.neighbors)
        
        for curr in clones:
            clones[curr].neighbors = [clones[c] for c in curr.neighbors]
        
        return clones[node]
        
