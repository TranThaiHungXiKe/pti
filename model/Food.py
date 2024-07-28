import webbrowser
import json

class cook:
     def __init__(self,id,name,date,score,link):
         self.id = id
         self.name = name
         self.date = date
         self.score = score
         self.link = link

     def show(self):
         print(self.id,"-",self.name,"-",self.date,"-",self.score,"-",self.link,"-")
        

     def getId(self):
         return self.id
     def getName(self):
         return self.name
     def getDate(self):
         raise self.date


     def open_cook(self):
         webbrowser.open(self.link)

class food:
     def __init__(self):
        self.list = []
        self.loadAllFood()                                                                                                                               
     def getAllfood(self):
         return self.list
     def add_food(self,cook):
         self.list.append(cook)
     def show_all_food(self):
         for i in self.list:
             i.show()
     def saveAllfood(self):
            jsonfile = list()
            for account in self.list:
                jsonfile.append(account.__dict__)
            with open("food.json","w") as file:
                json.dump(jsonfile, file ,indent=2)
     def loadAllFood(self):
    
             with open ("data/food.json","r") as file:
                 jsonfile = json.load(file)
                 for cok in jsonfile:
                     Cook = cook(cok["id"],cok["name"],cok["date"],cok["score"],cok["link"])
                     self.add_food(Cook)
    


