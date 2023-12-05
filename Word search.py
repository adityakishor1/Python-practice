class Solution(object):
    def exist(self, board, word):
        def getNeighbor(i, j):
            opt = []
            if i+1<M: opt.append((i+1, j))
            if j+1<N: opt.append((i, j+1))
            if i-1>=0: opt.append((i-1, j))
            if j-1>=0: opt.append((i, j-1))
            return opt

        def dfs(i, j, l):
            if l==len(word)-1 and board[i][j]==word[l]: return True
            if board[i][j]!=word[l]: return False

            char = board[i][j]
            board[i][j] = '#'

            for ni, nj in getNeighbor(i, j):
                if dfs(ni, nj, l+1): return True

            board[i][j] = char
            return False

        M = len(board)
        N = len(board[0])

        for i in xrange(M):
            for j in xrange(N):
                if dfs(i, j, 0): return True

        return False
