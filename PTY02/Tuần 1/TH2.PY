class Account:
    def __init__ (self,username ="",password ="" ) :
        self.us = username
        self.pa = password

    def show(self):
        print(self.us)
        print(self.pa)

    def login(self,inputusername,inputpassword):
        if self.us == inputusername and self.pa == inputpassword:
            print("Đăng nhập thành công")
        else:
            print("Đăng nhập thất bại")
    def changepassword(self,inputUS,inputOLDPW,inputNewPW):
        if inputUS == self.us and self.pa == inputOLDPW:
            self.pw = inputNewPW
            print("Đúng mật khẩu , nhập mật khẩu mới : ")
        else:
            print("Sai mật khẩu")







        