
class Task:
    def __init__(self, name, description):
        self.description = description
        self.name = name

    def printcommmand(self):
        print('it worked')

    def getname(self):
        return self.name

    def setname(self, newname):
        self.name = newname


    def getdesc(self):
        return self.description
