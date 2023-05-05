import random

class Helpers:

    def gameInput(inputMessage, returnType='int'):

        while True:
            try:
                inputValue = int(input(inputMessage)) if returnType == 'int' else input(inputMessage)
                return inputValue
            except :
                print("\n Hatalı Giriş Yaptınız, Lütfen Tekrar Giriş Yapınız ")
                continue


    def randomColor():
        randomNumber = random.random()
        if randomNumber < 0.5:
            return ["Mavi","Kırmızı"]
        return ["Kırmızı","Mavi"]   

    def welcomePage():
        print("|------------------------------------|")
        print("|   Connect 4 Oyununu Hoş geldiniz   |")
        print("|------------------------------------|")
        print("|     Lütfen Oyun seçimi Yapınız     |")
        print("|------------------------------------|")
        print("|        1- Oynamaya Devam Et        |") 
        print("|        2- Yeni Oyun                |")
        print("|        3- Çıkış Yap                |")  
        print("|------------------------------------|")     

    def finishPage(wonPlayer=0):

        if wonPlayer == 0:
            print("|------------------------------------|")
            print("|           Oyun Sona Erdi           |")
            print("|------------------------------------|")
            print("|             BERABERLİK             |")
            print("|------------------------------------|")
        else :
            print("|------------------------------------|")
            print("|           Oyun Sona Erdi           |")
            print("|------------------------------------|")
            print(f"|              {wonPlayer}. Oyuncu             |")
            print("|------------------------------------|")