class Solution(object):
    def regionsBySlashes(self, grid):
        region = 1
        dsu = DSU()
        N = len(grid)
        
        #Union the border lines
        for i in xrange(N):
            dsu.union((i, 0), (i+1, 0))
            dsu.union((i, N), (i+1, N))
        for j in xrange(N):
            dsu.union((0, j), (0, j+1))
            dsu.union((N, j), (N, j+1))

        #Iterate through slashes and connect the dots
        #If the slash connects two already connected dots, the region will increament by one
        for i, row in enumerate(grid):
            for j, slash in enumerate(row):
                if slash=='/':
                    if not dsu.union((j+1, i), (j, i+1)):
                        region += 1
                elif slash=='\\':
                    if not dsu.union((j, i), (j+1, i+1)):
                        region += 1
        return region
