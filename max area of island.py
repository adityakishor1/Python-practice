class Solution(object):
    def maxAreaOfIsland(self, grid):
        def dfs(i0, j0):
            stack = [(i0, j0)]
            area = 0
            
            while stack:
                i, j = stack.pop()
                if grid[i][j]==0 or grid[i][j]==2: continue
                grid[i][j] = 2
                area += 1
                
                if i+1<M: stack.append((i+1, j))
                if 0<=i-1: stack.append((i-1, j))
                if j+1<N: stack.append((i, j+1))
                if 0<=j-1: stack.append((i, j-1))
            
            return area
                
        if not grid or not grid[0]: return 0
        
        max_area = 0
        M = len(grid)
        N = len(grid[0])
        
        for i in xrange(M):
            for j in xrange(N):
                if grid[i][j]==0 or grid[i][j]==2: continue
                max_area = max(max_area, dfs(i, j))
                
        return max_area
