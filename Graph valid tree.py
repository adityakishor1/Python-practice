class Solution(object):
	def validTree(self, n, edges):
		def union(n1, n2): #[2]
			n1_root = find(n1)
			n2_root = find(n2)
			if n1_root==n2_root: return True
			markset[n2_root] = n1_root
			return False

		def find(node): #[1]
			if markset[node]==-1: return node
			return find(markset[node])

		if len(edges)!=n-1: return False
		markset = [-1 for _ in xrange(n)] #[0]

		for edge in edges:
			if union(edge[0], edge[1]): return False

		return True
