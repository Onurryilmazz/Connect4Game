class GameBoard:
    
    def __init__(self):
        self.table = []

    def showTable(self):
        """
        Ekrana Oyun tablosunu basan fonksiyon
        """

        self._readTable()
        print("1 2 3 4 5 6 7 8 9")
        print("* * * * * * * * *\n")
        for row in self.table:
            for column in row:
                print(column,end=" ")
            print()

    def _readTable(self):
        """
        Txt dosyasından oyun tahtasını okuyan fonksiyon
        """

        with open("Tahta.txt","r") as f:
            tx = []
            a = f.readlines()
            for row in a:
                rowTable = row.split()
                tx.append(rowTable)
        self.table = tx
    
    def _readAction(self):
        """
        Txt dosyasından oyun tahtasını okuyan fonksiyon
        """

        with open("Hamle.txt","r") as f:
            actions = []
            a = f.readlines()
            for row in a:
                rowTable = row.split()
                actions.append(rowTable)
        return actions

    def createEmptyTable(self): 
        """
        Boş Oyun Tahtası yaratan fonksiyon
        """
        
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
        """
        Oynanan slotun bulunduğu kolonun uygunluğunu kontrol eden fonksiyon
        """

        try:
            if self.table[0][column-1] == '-' and column != 0 :
                return True
            return False
        except:
            print("\n Girdiğiniz Değer Oyun Alanı Dışındadır, Tekrar Giriş Yapınız")
    
    def updateAction(self,column,color):
        """
        Oyuncuların Hamleleri sonucu Oyun Tahtasını güncelleyen Fonksiyon 
        """

        for index,row in enumerate(self.table[::-1],1):
            if row[int(column)-1] == "-":
                self.table[-index][int(column)-1] = color[0]
                self.writeTahtaTxt()
                self._actionLog(len(self.table)-index+1,column,color[0])
                return len(self.table)-index,column-1
            
    def _actionLog(self,row,column,color):     
        """
        Her Hamlenin Loglarını Txt dosyasına yazan fonksiyon
        """   

        with open("Hamle.txt","a") as f:
            hamle = str(row)+str(column)+'-'+color
            f.write(f"\n{hamle}")

    def winControl(self,color,row,column):
        """
        Oyuncuların hamlesinin kazanma durumunu kontrol eden fonksiyon
        """

        rowSlotList = self._getRowSlots(row)
        if self._slotControl(rowSlotList,color):
            return True
        
        columnSlotList = self._getColumnSlots(column)
        if self._slotControl(columnSlotList,color):
            return True
        
        crossSlotListLeftDiagonal, crossSlotListRightDiagonal = self._getCrossSlots(column,row)

        if self._slotControl(crossSlotListLeftDiagonal,color):
            return True
        
        if self._slotControl(crossSlotListRightDiagonal,color):
            return True
        
        return False

    def _slotControl(self,slotList,color):
        """
        Verilen listede slotların kazanma durumunu kontrol eden fonksiyon
        """
        numberOfSequentialSlots = 0
        for slot in slotList:
            if slot == color[0]:
                numberOfSequentialSlots += 1
                if numberOfSequentialSlots >= 4:
                    return True
                continue
            else:    
                numberOfSequentialSlots = 0
        
        if numberOfSequentialSlots >= 4:
            return True
        return False
               
    def _getRowSlots(self,row):
        """
        Oynanan Hamlenin satırını kontrol eden fonksiyon
        """
        return self.table[row]
    
    def _getColumnSlots(self,column):
        """
        Oynanan Hamlenin sütununu kontrol eden fonksiyon
        """
        columnSlots = []
        for row in self.table:
            columnSlots.append(row[column])
        return columnSlots
  
    def _getCrossSlots(self,column,row):
        """
        Oynanan Hamlenin çapraz yönlerini kontrol eden fonksiyon
        """
        diagonalValues = []
        leftDiagonal= []
        rightDiagonal = []

        # sol üst köşegen
        for i in range(min(row, column)):
            diagonalValues.append(self.table[row-i-1][column-i-1])

        leftDiagonal.extend(diagonalValues[::-1])
        leftDiagonal.append(self.table[row][column])
        diagonalValues = []

        # sağ alt köşegen
        for i in range(min(len(self.table)-row-1, len(self.table)-column-1)):
            diagonalValues.append(self.table[row+i+1][column+i+1])
        leftDiagonal.extend(diagonalValues)    
        

        #sağ üst kçşegen
        diagonalValues = []
        for i in range(min(row, len(self.table)-column-1)):
            diagonalValues.append(self.table[row-i-1][column+i+1])

        rightDiagonal.extend(diagonalValues[::-1])
        rightDiagonal.append(self.table[row][column])
        diagonalValues = []

        # sol alt köşegen
        for i in range(min(len(self.table)-row-1, column)):
            diagonalValues.append(self.table[row+i+1][column-i-1])
        rightDiagonal.extend(diagonalValues)
        
        return leftDiagonal,rightDiagonal

    def writeTahtaTxt(self):
        """
        Txt Dosyasına oyun tahtasının durumunu yazan fonksiyon
        """

        with open("Tahta.txt","w") as f:
            for row in self.table:
                for column in row:
                    f.write(column + ' ')
                f.write("\n")

    def startOldGame(self):
        self._readTable()
        oldGameValues = {}

        oldAction = self._readAction()
        oldGameRedSlot,oldGameBlueSlot,lastActionColor = self._getOldGameSlot(oldAction)

        if lastActionColor == "Kırmızı":
            oldGameValues["user1Color"] = "Mavi"
            oldGameValues["user2Color"] = "Kırmızı"

            oldGameValues["user1Slot"] = oldGameBlueSlot
            oldGameValues["user2Slot"] = oldGameRedSlot
        
        else : 
            oldGameValues["user2Color"] = "Mavi"
            oldGameValues["user1Color"] = "Kırmızı"

            oldGameValues["user2Slot"] = oldGameBlueSlot
            oldGameValues["user1Slot"] = oldGameRedSlot

        return oldGameValues

    def _getOldGameSlot(self,acitonList):

        colorRedSlot = 40
        colorBlueSlot = 40
        lastActionColor = ""

        for action in acitonList:
            if len(action) == 0:
                continue
            if "M" in action[0]:
                colorBlueSlot -= 1
                lastActionColor = "Mavi"
            elif "K" in action[0]:
                colorRedSlot -= 1
                lastActionColor = "Kırmızı"

        return colorRedSlot,colorBlueSlot,lastActionColor
        