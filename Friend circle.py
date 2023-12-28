class Solution(object):
    def findCircleNum(self, M):
        if not M or not M[0]: return 0
        count = 0
        visited = set()
        
        for student in xrange(len(M)):
            if student in visited: continue
            
            count += 1

            #dfs
            stack = [student]
            while stack:
                curr_student = stack.pop()
                if curr_student in visited: continue
                visited.add(curr_student)
                stack.extend([class_mate for class_mate, is_friend in enumerate(M[curr_student]) if is_friend])
                
        return count
