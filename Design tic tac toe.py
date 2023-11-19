class TicTacToe(object):

    def __init__(self, n):
        self.records = [[[0]*n, [0]*n, 0, 0], [[0]*n, [0]*n, 0, 0]]
        self.n = n
        
        
    def move(self, row, col, player):
        record = self.records[player-1]
        record[0][row] += 1
        record[1][col] += 1
        if row==col: record[2] += 1
        if row+col==self.n-1: record[3] += 1

        if self.checkRecord(record, row, col): return player
            
        return 0
        
    def checkRecord(self, record, row, col):
        if record[0][row]==self.n: return True
        if record[1][col]==self.n: return True
        if record[2]==self.n: return True
        if record[3]==self.n: return True
        
        return False
