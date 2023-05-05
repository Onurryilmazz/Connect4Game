class GameBoard:
    
    def __init__(self):
        self.table = []

    def showTable(self):
        self.readTable()
        for row in self.table:
            for column in row:
                print(column,end=" ")
            print()

    def readTable(self):
        with open("Tahta.txt","r") as f:
            tx = []
            a = f.readlines()
            for row in a:
                rowTable = row.split()
                tx.append(rowTable)
        self.table = tx
    
    def createEmptyTable(self): 
        self.table = []

        for row in range(9):
            row = []
            for column in range(9):
                row.append('-')
            self.table.append(row)
        self.writeTahtaTxt()

        with open("Hamle.txt","a") as f:         
            f.truncate(0)

    def checkAction(self,column):
        try:
            if self.table[0][column-1] == '-' and column != 0 :
                return True
            return False
        except:
            print("\n Girdiğiniz Değer Oyun Alanı Dışındadır, Tekrar Giriş Yapınız")
    
    def updateAction(self,column,color):

        for index,row in enumerate(self.table[::-1],1):
            if row[int(column)-1] == "-":
                self.table[-index][int(column)-1] = color[0]
                self.writeTahtaTxt()
                self._actionLog(len(self.table)-index+1,column,color[0])
                return len(self.table)-index,column-1
            
    def _actionLog(self,row,column,color):        
            with open("Hamle.txt","a") as f:
                hamle = str(row)+str(column)+'-'+color
                f.write(f"\n{hamle}")

    def winControl(self,color,row,column):
        pass

               
    def _getRowSlots(self,row):
        return self.table[row]
    
    def _getColumnSlots(self,column):
        columnSlots = []
        for row in self.table:
            columnSlots.append(row[column])
        return columnSlots

    def _getCrossSlots(self,column,row):
        columnSlotsLeft = []
        columnSlotsRight = []

        #Oynanan taşın Sol üst ve Sağ alt çaprazlarının listesi
        for row in self.table[row::-1]:
            if column > 9 or column < 0:
                break
            columnSlotsLeft.append(row[column])
            column -= 1

        for row in self.table[row::]:
            if column+1 > 8 or column+1 < 0:
                break
            columnSlotsLeft.append(row[column+1])
            column += 1

        #Oynanan taşın Sol Alt ve Sağ Üst çaprazlarının listesi
        for row in self.table[row::-1]:
            if column > 9 or column < 0:
                break
            columnSlotsRight.append(row[column])
            column += 1

        for row in self.table[row::]:
            if column+1 > 8 or column+1 < 0:
                break
            columnSlotsRight.append(row[column+1])
            column -= 1

        return columnSlotsRight,columnSlotsLeft

    def writeTahtaTxt(self):

        with open("Tahta.txt","w") as f:
            for row in self.table:
                for column in row:
                    f.write(column + ' ')
                f.write("\n")
