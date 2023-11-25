class Solution(object):
    def calcEquation(self, equations, values, queries):
        def findVal(query):
            n1, n2 = query
            if n1 not in graph or n2 not in graph: return -1.0
            
            stack = [(n1, 1.0)] #[1]
            visited = set() #[4]
            
            while stack:
                n, val = stack.pop()
                visited.add(n)
                if n==n2:
                    return val
                else:
                    for nb, nb_val in graph[n]: #nb means neighbor
                        if nb not in visited:
                            stack.append((nb, nb_val*val)) #[3]
                            if n!=n1: graph[n1].append((nb, nb_val*val)) #[5]
            return -1.0
