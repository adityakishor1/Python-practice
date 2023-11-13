from collections import defaultdict, deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        inbound = defaultdict(int)
        q = deque()
        order = deque()
        
		#building graph as adjacency list
        for c1, c2 in prerequisites:
            graph[c2].append(c1)
            inbound[c1] += 1
        
		#find the starting point
        for c in xrange(numCourses):
            if inbound[c]==0:
                q.append(c)
        
		#traverse the directed graph
        while q:
            c = q.popleft()
            
            for nei in graph[c]:
                inbound[nei] -= 1
                if inbound[nei]==0:
                    q.append(nei)
                    
            order.append(c)
        
        return order if len(order)==numCourses else []
