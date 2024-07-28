class hinhchunhat:
    def __init__(self,Chieudai,Chieurong):
        self.chieudai = Chieudai
        self.chieurong = Chieurong

  
    def tinhchuvi(self):
        self.chuvi = 2 * (self.Chieudai + self.Chieurong)
            
    def tinhdientich(self):
        self.dientich = self.Chieudai * self.Chieurong
       
    def show(self):
        print(self.chuvi)
        print(self.dientich)

CN1 = hinhchunhat()
CN1.show()


   

