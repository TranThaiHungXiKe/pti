import webbrowser
import json

class cook:
     def __init__(self,id,name,date,score,link, img, recipe,information):
         self.id = id
         self.name = name
         self.date = date
         self.score = score
         self.link = link
         self.img = img
         self.recipe = recipe
         self.information = information

     def show(self):
         print(self.id,"-",self.name,"-",self.date,"-",self.score,"-",self.link,"-",self.img,"-")
        

     def getId(self):
         return self.id
     def getName(self):
         return self.name
     def getDate(self):
         return self.date
     def getScore(self):
         return self.score
     def getLink(self):
         return self.link
     def getImg(self):
         return self.img
     def getRecipe(self):
         return self.recipe
     def getInformation(self):
         return self.information
         


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
         self.saveAllfood()
     def delete_food_by_name(self,name_food):
         for food in self.list :
             if food.getName() == name_food:
                 self.list.remove (food)
         self.saveAllfood()
     def edit_food_by_name(self,nameoldcook,newcook):
          for food in self.list :
             if food.getName() == nameoldcook:
                 self.list.remove (food)
                 self.list.append(newcook)
          self.saveAllfood()
     def show_all_food(self):
         for i in self.list:
             i.show()
     def saveAllfood(self):
            jsonfile = list()
            for account in self.list:
                jsonfile.append(account.__dict__)
            with open("data/food.json","w") as file:
                json.dump(jsonfile, file ,indent=8)
                          
     def searchfoodbyname(self,name):
         result = []
         for cook in self.list:
             if name in cook.getName():
                 result.append(cook)
                 cook.show()
         return result
             
         
     def loadAllFood(self):
    
             with open ("data/food.json","r") as file:
                 jsonfile = json.load(file)
                 for cok in jsonfile:
                     Cook = cook(cok["id"],cok["name"],cok["date"],cok["score"],cok["link"],cok["img"],cok["recipe"],cok["information"])
                     self.add_food(Cook)
     def getFoodbyname(self,nameFood):
         for Cook in self.list :
             if Cook.getName() == nameFood:
                 return Cook
     def sortFoodByName(self):
         self.list.sort(key= lambda cook: cook.getName())
         self.show_all_food()
     def sortFoodByScore(self):
         self.list.sort(key= lambda cook:int( cook.getScore()),reverse=True)
         self.show_all_food()
         
     

