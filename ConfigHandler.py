import json
class Handler():
    def __init__(self):
        self.filePath = "config.json"
        self.pyDict = {}
        self.updatePyDict()
   
    def updatePyDict(self):
        with open(self.filePath,"r") as file:
            self.pyDict = json.loads(file.read())

    def updateCommands(self,commands):
        for i,k in enumerate(self.pyDict.keys()):
            self.pyDict[k] = commands[i]
        with open(self.filePath,"w") as file:
            file.write(json.dumps(self.pyDict,indent=4))
    
    def getCommand(self,gesture):
        if gesture not in ["0","6"]:
            self.updatePyDict()
            return self.pyDict[gesture]
    
    def getAllCommands(self):
        self.updatePyDict()
        return list(self.pyDict.values())