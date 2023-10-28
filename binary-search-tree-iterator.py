class BSTIterator(object):

    def __init__(self, root):
        self.stack = []
        self.node = root
        
        

    def next(self):
        while self.node:
            self.stack.append(self.node)
            self.node = self.node.left
        self.node = self.stack.pop()
        returnVal = self.node.val
        self.node = self.node.right
        return returnVal
        
        

    def hasNext(self):
        return self.node or self.stack
