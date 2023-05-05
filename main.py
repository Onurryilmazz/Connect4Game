from GameBoard import * 
from User import *
from helpers import *
    

def startingGame():

    helpers = Helpers

    helpers.welcomePage()
    selectedGame = helpers.gameInput(inputMessage=" Seçiminizi Giriniz :  ",returnType='str')

    if selectedGame == "1":
        print("\n<---- Eski Oyun Yükleniyor ---->\n")
        
    elif selectedGame == "2" :
        print("\n<---- Yeni Oyun Başlatılıyor ---->\n")

        userColor = helpers.randomColor()
        user1 = User(1,userColor[0])
        user2 = User(2,userColor[1])
        gameBoard = GameBoard()
        gameBoard.createEmptyTable()
    
        gamePlayer = user1

        while user1.userPul + user2.userPul > 0:
            gameBoard.showTable()
            print(f"\n Hamle Yapılan Pul : {gamePlayer.userColor} \n")
            action = helpers.gameInput(inputMessage="\nHamlenizi Giriniz : ",returnType='int')
            
            while True:
                if gameBoard.checkAction(action):
                    break
                action = helpers.gameInput(inputMessage="\nBu alana hamle yapılamamaktadır. Yeni Hamleniz : ",returnType='int')

            lastActionRow,lastActionColumn = gameBoard.updateAction(action,gamePlayer.userColor)

            if gameBoard.winControl(gamePlayer.userColor):
                helpers.finishPage(gamePlayer.userId)
                return
            gamePlayer.reducePul()
            gamePlayer = user2 if gamePlayer.userId == user1.userId else user1

        print("\nOyun Sonu\n")
        gameBoard.showTable() 
        print()
        helpers.finishPage()   
        
    else:
        print("Program Sonlandı")


    

startingGame()
# finishPage(1)

