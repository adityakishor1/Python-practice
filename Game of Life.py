class Solution(object):
    def gameOfLife(self, board):
        if board==None or len(board)==0 or len(board[0])==0: return board

        m = len(board)
        n = len(board[0])
        
        def count_alive(i, j):
            if i<0 or j<0 or i>=m or j>=n: return 0
            count = 0

            #bottom, top, right, left
            if i+1<m: count+=board[i+1][j]%2 #[0]
            if 0<=i-1: count+=board[i-1][j]%2
            if j+1<n: count+=board[i][j+1]%2
            if 0<=j-1: count+=board[i][j-1]%2

            #bottomright, topleft, bottomleft, topright
            if i+1<m and j+1<n: count+=board[i+1][j+1]%2
            if 0<=i-1 and 0<=j-1: count+=board[i-1][j-1]%2
            if i+1<m and 0<=j-1: count+=board[i+1][j-1]%2
            if 0<=i-1 and j+1<n: count+=board[i-1][j+1]%2

            return count

        for i in xrange(m): #[1]
            for j in xrange(n):
                count = count_alive(i, j) #[2]

                if board[i][j]==1:
                    if count<2 or count>3:
                        board[i][j] = 3
                elif board[i][j]==0:
                    if count==3:
                        board[i][j] = 2

        for i in xrange(m): #[3]
            for j in xrange(n):
                if board[i][j]==2:
                    board[i][j] = 1
                elif board[i][j]==3:
                    board[i][j] = 0

        return board
