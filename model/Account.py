import json
class Account:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def show(self):
        print("US:",self.username,"PW",self.password)

    def getUserName(self):
        return self.username
    def getPassWord(self):
        return self.password
class ListAccount:
    def __init__(self):
        self.list = []
        self.loadAllAccount()
    def addAccount(self,account):
        self.list.append(account.getUserName()+ ":" +account.getPassWord())
    def showAllAccount(self):
        for account in self.list:
            account.show()
    def changePasswordAccount(self,username,password,newpassword):
        for account in self.list:
            if account.username == username:
                if account.password == password:
                    account.setNewPassword(newpassword)
                else:
                    print("wrong password !!!!")
    def saveAllAccount(self):
            jsonfile = list()
            for account in self.list:
                ["123:123","use:ps"]
                pos = account.find(":") 
                us = account[:pos]
                ps = account[pos+1:]
                newAccount = Account(us,ps)
                jsonfile.append(newAccount.__dict__)
            with open("data/account.json","w") as file:
                json.dump(jsonfile, file ,indent=2)
    def checkAccount(self,account):
       return (account.getUserName() + ":" + account.getPassWord()) in self.list
    def loadAllAccount(self):
        with open("data/account.json","r") as file:
            jsonFile = json.load(file)

            for account in jsonFile:
                self.list.append(account["username"]+":"+ account ["password"])




