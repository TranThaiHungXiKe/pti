from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox,QDialog
from PyQt6 import uic
from PyQt6.QtCore import QDate , QDateTime
import sys
import os

from model.Account import Account , ListAccount  
from ui_py.MainPage import Ui_MainWindow
from ui_py.dashboardform import Ui_MainWindow
from model.Food import cook , food



# Hàm hiển thị thông báo
def show_message_box(title, message, icon):
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setIcon(icon)
    msg_box.setText(message)
    msg_box.exec()
# Class trang đăng nhập
class AddDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("./ui/add.ui",self)
        self.btnbox.accepted.connect(self.addFood)
    def addFood(self):
        self.L = food()
        self.L.add_food(cook("null",self.txtFOOD.text(),self.txtDate.text(),self.txtImage.text(),self.txtScore.text()))
        home.callAfterInit()
class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.oldFood = None
        uic.loadUi("./ui/edit.ui",self)
        self.buttonBox.accepted.connect(self.setNewFood)
    def setOldfood(self,cook:cook):
        self.oldFood = cook
        self.txtname.setText(cook.getName())
        date_str = cook.getDate()
        date = QDate.fromString(date_str,"yyyy-MM-dd")
        self.txtdate.setDate(date)
        self.txtScore.setText(cook.getScore())
        self.txtUrl.setText(cook.getLink())

    def setNewFood(self):
        self.L = food()
        self.L.delete_food_by_name(self.oldFood.getName())

        self.L.add_food(cook("Null",self.txtname.text(),self.txtdate.text(),self.txtScore   .text(),self.txtUrl.text()))
        home.callAfterInit()
        self.close()
    
class HomeMenuDashboard(QMainWindow,Ui_MainWindow):
    def __init__ (self):
        super().__init__()
        self.setupUi(self)
        self.callAfterInit()
        self.btnXoaDialog.clicked.connect(self.deletefood)
        self.btnChinhSuaDialog.clicked.connect(self.showEditDialog)
        self.btnAddDialog.clicked.connect(self.showAddDialog)
        self.btnsearch.clicked.connect(self.searchFood)
    def deletefood(self):
        nameFoodDelete = self.List_cook.currentItem().text()
        self.List_cook.takeItem(self.List_cook.currentRow())
        self.L.delete_food_by_name(nameFoodDelete)
        self.callAfterInit
    def showAddDialog(self):
        add.show()

    def showEditDialog(self):

        if self.List_cook.currentRow():
          edit.setOldfood(self.L.getFoodbyname(self.List_cook.currentItem().text()))
          edit.show()

    def callAfterInit(self):
        self.L = food()
        self.List_cook.clear()
        for cok in self.L.getAllfood():
            self.List_cook.addItem(cok.getName())
    def searchFood(self):
        valueSearch = self.ValueSearch.text()
        dataSearch = self.L.searchfoodbyname(valueSearch) #--> list object
        self.List_cook.clear()
        for cok in dataSearch:
            self.List_cook.addItem(cok.getName())

class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/LoginPage.ui",self) # Load Giao diện từ file .ui
        self.L = ListAccount()

        # ====== Kết nối sự kiện ở đây
        self.pushButton_login.clicked.connect(self.checkLogin)
        self.pushButton_createAccount.clicked.connect(self.showSignupPage)
    def showSignupPage(self):
        signupPage.show()  # Hiển thị trang đăng ký
        self.close()       # Ẩn đi trang đăng nhập
    # Hàm kiểm tra đăng nhập
    def checkLogin(self):

       print(self.L.checkAccount(Account(self.lineEdit_Fullname.text(), self.lineEdit_Password.text(),)))
       print(self.lineEdit_Fullname.text() , self.lineEdit_Password.text() ) 
       if self.L.checkAccount(Account(self.lineEdit_Fullname.text(), self.lineEdit_Password.text(),)) == True:
           mainPage.show()
           self.close()

               

class SigninPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/SigninPage.ui",self) 
        self.L = ListAccount()
    
    
               
              # ====== Kết nối sự kiện ở đây
        #self.pushButton_Gologin.clicked.connect(self.showLoginPage)
        self.pushButton_Signup.clicked.connect(self.registerAccount)
    def showLoginPage(self):
        loginPage.show()  # Hiển thị trang đăng nhập
        self.close()      # Ẩn đi trang đăng ký
 # Hàm đăng ký tài khoản
    def registerAccount(self):
        username = self.lineEdit_Fullname.text()
        password = self.lineEdit_Password.text()
        confirmPassword = self.lineEdit_Confirm_Password.text()
    
        if not username or not password or not confirmPassword:
            show_message_box("Lỗi", "Vui lòng nhập đầy đủ thông tin.", QMessageBox.Icon.Warning)
            return

        if password != confirmPassword:
            show_message_box("Lỗi", "Mật khẩu không khớp! Vui lòng nhập lại.", QMessageBox.Icon.Warning)
            return

        self.L.addAccount(Account(username,password))
        self.L.saveAllAccount()
     # Hàm lưu tài khoản vào file users.txt
    def saveAccount(self, username, password):
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file:
                for line in file:
                    stored_username, _ = line.strip().split(",")
                    if username == stored_username:
                        return False  # Tài khoản đã tồn tại

        with open("users.txt", "a") as file:
            file.write(f"{username},{password}\n")
        return True


class MainPage(QMainWindow):
      def __init__(self):
        super().__init__()
        uic.loadUi("ui/MainPage.ui",self) # Load Giao diện từ file .ui
           # ====== Kết nối sự kiện ở đây
        self.pushButton_recipe_Thitkho.clicked.connect(self.showProductPage1)
        self.pushButton_book_thitkho.clicked.connect(self.showProductPage2)
        self.pushButton_recipe_gachien.clicked.connect(self.showProductPage3)
        self.pushButton_book_gachien.clicked.connect(self.showProductPage4)
        
       # Hàm chuyển sang trang sản phẩm 1
      def showProductPage1(self):
         productPage1.show()
         self.close()
         # Hàm chuyển sang trang sản phẩm 2
      def showProductPage2(self):
         productPage2.show()
         self.close()
      # Hàm chuyển sang trang sản phẩm 3
      def showProductPage3(self):
         productPage3.show()
         self.close()
      # Hàm chuyển sang trang sản phẩm 4
      def showProductPage4(self):
         productPage4.show()
         self.close()


# Class trang sản phẩm 1
class ProductPage1(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ProductPage1.ui",self) # Load Giao diện từ file .ui
         # ====== Kết nối sự kiện ở đây
        self.pushButton_Thitkho.clicked.connect(self.mainpage)
    
    def mainpage (self):
        mainPage.show()
        self.close()
class ProductPage2(QMainWindow): 
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ProductPage1Book.ui",self)
          # ====== Kết nối sự kiện ở đây
        self.pushButton_Thitkho_book.clicked.connect(self.mainpage)
    def mainpage (self):
        mainPage.show()
        self.close()

class ProductPage3(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ProductPage2.ui",self)
           # ====== Kết nối sự kiện ở đây
        self.pushButton_return_gachien.clicked.connect(self.mainpage)
    def mainpage (self):
        mainPage.show()
        self.close()

class ProductPage4(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ProductPage2Book.ui",self)
           # ====== Kết nối sự kiện ở đây
        self.pushButton_return_gachien_book.clicked.connect(self.mainpage)
    def mainpage (self):
        mainPage.show()
        self.close()


    


    def mainpage (self):
        mainPage.show()
        self.close()

    
    def mainpage (self):
        mainPage.show()
        self.close()


    
    def mainpage (self):
        mainPage.show()
        self.close()
    
    def mainpage (self):
        mainPage.show()
        self.close()
          
    
    def mainpage (self):
        mainPage.show()
        self.close()

        
    
    def mainpage (self):
        mainPage.show()
        self.close()
    
       




if __name__ == "__main__":
    app = QApplication(sys.argv)

    loginPage = LoginPage() # Tạo đối tượng LoginPage
    signupPage = SigninPage() # Tạo đối tượng SignupPage
    mainPage = MainPage()
    home = HomeMenuDashboard()
    productPage1 = ProductPage1()
    productPage2 = ProductPage2()
    productPage3 = ProductPage3()
    productPage4 = ProductPage4()
    add = AddDialog()
    edit = EditDialog()


    home.show() # Hiển thị trang đăng nhập

    sys.exit(app.exec())
