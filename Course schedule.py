class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = {n:[] for n in xrange(numCourses)} #[0]
        
        for n1, n2 in prerequisites:
            graph[n1].append(n2)
        
        for target_course in xrange(numCourses): #[1]
            stack = graph[target_course]
            visited = set()
            while stack:
                course = stack.pop()
                visited.add(course)
                if course==target_course: return False
                for ajc in graph[course]:
                    if ajc not in visited:
                        stack.append(ajc)
        return True
