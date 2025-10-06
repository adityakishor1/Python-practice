class Solution:
    def knightTour(self, n):
        board = [[-1 for _ in range(n)] for _ in range(n)]
        dx = [2, 1, -1, -2, -2, -1, 1, 2]
        dy = [1, 2, 2, 1, -1, -2, -2, -1]
        board[0][0] = 0
        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < n and board[x][y] == -1
        
        # Recursive backtracking function
        def solve(x, y, movei):
            if movei == n * n:
                return True  
            
            for k in range(8):
                next_x = x + dx[k]
                next_y = y + dy[k]
                if is_valid(next_x, next_y):
                    board[next_x][next_y] = movei
                    if solve(next_x, next_y, movei + 1):
                        return True
                    # Backtrack
                    board[next_x][next_y] = -1
            return False
        if solve(0, 0, 1):
            return board
        else:
            return []
