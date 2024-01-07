class Trie(object):

    def __init__(self):
        self.period = '.'
        self.root = Node('')
        

    def insert(self, word):
        word = word + self.period
        node = self.root
        
        for c in word:
            if c not in node.children:
                node.children[c] = Node(c)
            node = node.children[c]
        

    def search(self, word):
        word = word + self.period
        node = self.root
        
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
        

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
