class User :
    
    def __init__(self,userId,userColor) -> None:
        self.userId = userId
        self.userColor = userColor
        self.userPul = 40

    def reducePul(self):
        self.userPul -= 1

    def updatePul(self,pulValue):
        self.userPul = pulValue

    def printUserPulValue(self):
        print(self.userPul)