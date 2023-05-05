class User :
    
    def __init__(self,userId,userColor) -> None:
        self.userId = userId
        self.userColor = userColor
        self.userPul = 40

    def reducePul(self):
        self.userPul -= 1