class FileSystem(object):

    def __init__(self):
        self.files = {}
        self.dirs = {}

    def ls(self, path):
        if path in self.files:
            return [path.split('/')[-1]]
        else:
            if path=='/': return sorted(self.dirs.keys())
            curr = self.dirs
            for d in path.split('/')[1:]:
                curr = curr[d]
            return sorted(curr.keys())
        
    def mkdir(self, path):
        curr = self.dirs
        for d in path.split('/')[1:]:
            if d not in curr:
                curr[d] = {}
            curr = curr[d]
        
    def addContentToFile(self, filePath, content):
        if filePath not in self.files:
            self.mkdir(filePath)
            self.files[filePath] = content
        else:
            self.files[filePath] += content
            
    def readContentFromFile(self, filePath):
        return self.files[filePath]
