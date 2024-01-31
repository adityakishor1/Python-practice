class Logger(object):

    def __init__(self):
        #stores the messages within 10 seconds
        self.q = collections.deque()
        self.set = set()
        

    def shouldPrintMessage(self, timestamp, message):
        while self.q and timestamp-self.q[0][0]>=10:
            time, msg = self.q.popleft()
            self.set.remove(msg)
        
        if message not in self.set:
            self.q.append((timestamp, message))
            self.set.add(message)
            return True
        else:
            return False
