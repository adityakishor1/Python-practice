class MinStack(object):

    def __init__(self):
        self.stack = []
        

    def push(self, x):
        self.stack.append((x, min(x, self.getMin())))
        

    def pop(self):
        if len(self.stack)==0: return None
        return self.stack.pop()[0]
        

    def top(self):
        if len(self.stack)==0: return None
        return self.stack[-1][0]
        

    def getMin(self):
        if len(self.stack)==0: return float('inf')
        return self.stack[-1][1]
        
