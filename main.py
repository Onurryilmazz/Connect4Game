from GameBoard import * 
from User import *
from helpers import *
    

def _gamePlay(user1: User,user2: User, gameBoard: GameBoard):

    helpers = Helpers
    gamePlayer = user1

    while user1.userPul + user2.userPul > 0:
            gameBoard.showTable()
            print(f"\nHamle Yapılan Pul : {gamePlayer.userColor} \n")
            action = helpers.gameInput(inputMessage="\nHamlenizi Giriniz : ",returnType='int')
            
            while True:
                if gameBoard.checkAction(action):
                    break
                action = helpers.gameInput(inputMessage="\nBu alana hamle yapılamamaktadır. Yeni Hamleniz : ",returnType='int')

            lastActionRow,lastActionColumn = gameBoard.updateAction(action,gamePlayer.userColor)

            if gameBoard.winControl(gamePlayer.userColor,lastActionRow,lastActionColumn):
                print("\nOyun Sonu\n")
                gameBoard.showTable() 
                print()
                helpers.finishPage(gamePlayer.userId,gamePlayer.userColor)
                return
            gamePlayer.reducePul()
            gamePlayer = user2 if gamePlayer.userId == user1.userId else user1

    print("\nOyun Sonu\n")
    gameBoard.showTable() 
    print()
    helpers.finishPage()  
    
def main():

    helpers = Helpers
    helpers.welcomePage()
    selectedGame = helpers.gameInput(inputMessage=" Seçiminizi Giriniz :  ",returnType='str')
    gameBoard = GameBoard()

    if selectedGame == "1":

        print("\n<---- Eski Oyun Yükleniyor ---->\n"),

        oldGameValues = gameBoard.startOldGame() 
        
        user1Color = oldGameValues["user1Color"]
        user2Color = oldGameValues["user2Color"]
        user1Slot = oldGameValues["user1Slot"]
        user2Slot = oldGameValues["user2Slot"]

        if gameBoard.checkLastGameEndStatus():
            helpers.finishPage(wonPlayer=-1,wonColor=user2Color)
            return 

        user1 = User(1,user1Color)
        user1.updatePul(user1Slot)

        user2 = User(2,user2Color)
        user2.updatePul(user2Slot)

        del user1Color,user2Color,user1Slot,user2Slot

        _gamePlay(user1,user2,gameBoard)

    elif selectedGame == "2" :
        print("\n<---- Yeni Oyun Başlatılıyor ---->\n")

        userColor = helpers.randomColor()
        user1 = User(1,userColor[0])
        user2 = User(2,userColor[1])
        gameBoard.createEmptyTable()
    
        _gamePlay(user1,user2,gameBoard)

    else:
        print("Program Sonlandı")


if __name__ == "__main__":
    main()
