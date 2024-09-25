from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox,QDialog , QWidget
from PyQt6 import uic, QtCore , QtGui , QtWidgets
from PyQt6.QtCore import QDate , QDateTime
import sys
import os

from model.Account import Account , ListAccount  
from ui_py.MainPage import Ui_MainWindow
from ui_py.dashboardform import Ui_MainWindow
from model.Food import cook , food
from ui_py.ui_sortingpage import Ui_sorting
from ui_py.ui_recipe import Ui_recipe

# from AI.Listen_and_Speak import speech_to_text




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
        self.pushButton_browse.clicked.connect(self.browseImage)
        self.pushButton_browse_URL.clicked.connect(self.browseURLvid)

    def browseURLvid (self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, " select an video", "" , "Image Files (*.mp4 *.jpg *.bmp )")

        if filePath:
            self.txtScore.setText(filePath)

    def browseImage (self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, " select an Image", "" , "Image Files (*.png *.jpg *.bmp )")

        if filePath:
            self.txtImage.setText(filePath)
    def addFood(self):
        self.L = food()
        self.L.add_food(cook("null",self.txtFOOD.text(),self.txtDate.text(),self.txtImage.text(),self.txtScore.text(),self.txtImage.text(),self.txt_recipe.text(),self.txtInformation.text()))
        home.callAfterInit()
        sorTing.loadDataObjects()
class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.oldFood = None
        uic.loadUi("./ui/edit.ui",self)
        self.buttonBox.accepted.connect(self.setNewFood)
        self.pushButton_browse.clicked.connect(self.browseImage)
    def browseImage (self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, " select an Image", "" , "Image Files (*.png *.jpg *.bmp )")

        if filePath:
          self.txtImage.setText(filePath)
    def setOldfood(self,cook:cook):
        self.oldFood = cook
        self.txtname.setText(cook.getName())
        date_str = cook.getDate()
        date = QDate.fromString(date_str,"yyyy-MM-dd")
        self.txtdate.setDate(date)
        self.txtUrl.setText(cook.getLink())
        self.txtImage.setText(cook.getImg())
        self.txt_edit_recipe.setText(cook.getRecipe())
        self.txtUrl_edit_information.setText(cook.getInformation())

    def setNewFood(self):
        self.L = food()
        self.L.delete_food_by_name(self.oldFood.getName())

        self.L.add_food(cook("Null",self.txtname.text(),self.txtdate.text(),"10",self.txtUrl.text(),self.txtImage.text(),self.txt_edit_recipe.text(),self.txtUrl_edit_information.text()))
        home.callAfterInit()
        sorTing.loadDataObjects()
        self.close()
class SorTing (QMainWindow,Ui_sorting):
    def __init__ (self):
         super().__init__()
         self.setupUi(self)
         self.l = food()
         self.loadDataObjects()
         self.pushButton_back.clicked.connect(self.ShowMainPage)
         self.pushButton_thitkho.clicked.connect(self.book_thit_kho)
         self.pushButton_recipe_Thitkho_2.clicked.connect(self.recipe_Thitkho)

    def recipe_Thitkho(self,z:cook):
        recipeThitkho.loadObject(z) 
        recipeThitkho.show()

    
    def book_thit_kho(self):
        bookThitKho.show()

    def ShowMainPage(self):
          mainPage.show()
          self.close()
    def loadDataObjects(self):
          self.setupUi(self)
          self.l = food()
          self.pushButton_back.clicked.connect(self.ShowMainPage)
          self.pushButton_thitkho.clicked.connect(self.book_thit_kho)
          for x in self.l.getAllfood():
            self.widget_2 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
            self.widget_2.setMinimumSize(QtCore.QSize(636, 608))
            self.widget_2.setStyleSheet("background-color: rgb(57, 60, 68)")
            self.widget_2.setObjectName("widget_2")
            self.widget_5 = QtWidgets.QWidget(parent=self.widget_2)
            self.widget_5.setGeometry(QtCore.QRect(10, 10, 611, 295))
            self.widget_5.setStyleSheet("background-color:rgb(31, 31, 31)")
            self.widget_5.setObjectName("widget_5")
            self.label_2 = QtWidgets.QLabel(parent=self.widget_5)
            self.label_2.setGeometry(QtCore.QRect(60, 0, 482, 281))
            self.label_2.setMinimumSize(QtCore.QSize(482, 281))
            self.label_2.setMaximumSize(QtCore.QSize(483, 292))
            self.label_2.setStyleSheet("background-color:  rgb(57, 60, 68)")
            self.label_2.setText("123")
            self.label_2.setPixmap(QtGui.QPixmap(x.getImg()))
            self.label_2.setScaledContents(True)
            self.label_2.setObjectName("label_2")
            self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.widget_2)
            self.lineEdit_3.setGeometry(QtCore.QRect(100, 460, 231, 51))
            font = QtGui.QFont()
            font.setPointSize(9)
            self.lineEdit_3.setFont(font)
            self.lineEdit_3.setStyleSheet("background-color:rgb(31, 31, 31);\n"
    "color: rgb(255, 255, 255);")
            self.lineEdit_3.setObjectName("lineEdit_3")
            self.label_16 = QtWidgets.QLabel(parent=self.widget_2)
            self.label_16.setGeometry(QtCore.QRect(120, 390, 21, 21))
            font = QtGui.QFont()
            font.setPointSize(19)
            self.label_16.setFont(font)
            self.label_16.setText("123")
            self.label_16.setPixmap(QtGui.QPixmap("D:/download/star.png"))
            self.label_16.setScaledContents(True)
            self.label_16.setObjectName("label_16")
            self.label_18 = QtWidgets.QLabel(parent=self.widget_2)
            self.label_18.setGeometry(QtCore.QRect(140, 390, 21, 21))

            font = QtGui.QFont()
            font.setPointSize(19)
            self.label_18.setFont(font)
            self.label_18.setText("123")
            self.label_18.setPixmap(QtGui.QPixmap("D:/download/star.png"))
            self.label_18.setScaledContents(True)
            self.label_18.setObjectName("label_18")
            self.label_7 = QtWidgets.QLabel(parent=self.widget_2)
            self.label_7.setGeometry(QtCore.QRect(100, 390, 21, 21))
            font = QtGui.QFont()
            font.setPointSize(19)
            self.label_7.setFont(font)
            self.label_7.setText("hihi")
            self.label_7.setPixmap(QtGui.QPixmap("D:/download/star.png"))
            self.label_7.setScaledContents(True)
            self.label_7.setObjectName("label_7")
            self.pushButton_book_thitkho_2 = QtWidgets.QPushButton(parent=self.widget_2)
            self.pushButton_book_thitkho_2.setGeometry(QtCore.QRect(290, 530, 71, 61))
            self.pushButton_book_thitkho_2.clicked.connect(self.book_thit_kho)
            font = QtGui.QFont()
            font.setPointSize(1)
            self.pushButton_book_thitkho_2.setFont(font)
            self.pushButton_book_thitkho_2.setText("")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("D:/download/book.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.pushButton_book_thitkho_2.setIcon(icon1)
            self.pushButton_book_thitkho_2.setIconSize(QtCore.QSize(100, 70))
            self.pushButton_book_thitkho_2.setObjectName("pushButton_book_thitkho_2")
            self.label_17 = QtWidgets.QLabel(parent=self.widget_2)
            self.label_17.setGeometry(QtCore.QRect(30, 370, 61, 51))
            font = QtGui.QFont()
            font.setPointSize(19)
            self.label_17.setFont(font)
            self.label_17.setText("")
            self.label_17.setPixmap(QtGui.QPixmap("D:/download/like.png"))
            self.label_17.setScaledContents(True)
            self.label_17.setObjectName("label_17")
            self.pushButton_recipe_Thitkho_2 = QtWidgets.QPushButton(parent=self.widget_2)
            self.pushButton_recipe_Thitkho_2.setGeometry(QtCore.QRect(200, 530, 71, 61))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.pushButton_recipe_Thitkho_2.setFont(font)
            self.pushButton_recipe_Thitkho_2.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("D:/download/recipe-book.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.pushButton_recipe_Thitkho_2.setIcon(icon)
            self.pushButton_recipe_Thitkho_2.setIconSize(QtCore.QSize(100, 60))
            self.pushButton_recipe_Thitkho_2.setObjectName("pushButton_recipe_Thitkho_2")
            self.pushButton_recipe_Thitkho_2.clicked.connect(lambda _, item=x: self.recipe_Thitkho(z = x))

            self.label_15 = QtWidgets.QLabel(parent=self.widget_2)
            self.label_15.setGeometry(QtCore.QRect(40, 460, 51, 61))
            font = QtGui.QFont()
            font.setPointSize(19)
            self.label_15.setFont(font)
            self.label_15.setText("")
            self.label_15.setPixmap(QtGui.QPixmap("D:/download/comment.png"))
            self.label_15.setScaledContents(True)
            self.label_15.setObjectName("label_15")
            self.label_13 = QtWidgets.QLabel(parent=self.widget_2)
            self.label_13.setGeometry(QtCore.QRect(160, 390, 21, 21))
            font = QtGui.QFont()
            font.setPointSize(19)
            self.label_13.setFont(font)
            self.label_13.setText("")
            self.label_13.setPixmap(QtGui.QPixmap("D:/download/star.png"))
            self.label_13.setScaledContents(True)
            self.label_13.setObjectName("label_13")
            self.label_19 = QtWidgets.QLabel(parent=self.widget_2)
            self.label_19.setGeometry(QtCore.QRect(130, 320, 401, 31))
            font = QtGui.QFont()
            font.setPointSize(19)
            self.label_19.setFont(font)
            self.label_19.setStyleSheet("color: rgb(255, 255, 255);")
            self.label_19.setObjectName("label_19")
            self.label_19.setText(x.getName())
            self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget_2)
            self.pushButton_2.setGeometry(QtCore.QRect(520, 520, 93, 81))

            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap("D:/download/play-button.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.pushButton_2.setIcon(icon2)
            self.pushButton_2.setIconSize(QtCore.QSize(80, 70))
            self.pushButton_2.setObjectName("pushButton_2")     
            self.pushButton_2.clicked.connect(lambda _, item=x: self.openlink(a = x))
            self.horizontalLayout_2.addWidget(self.widget_2)
    def openlink(self,a):
        a.open_cook()
class HomeMenuDashboard(QMainWindow,Ui_MainWindow):
    def __init__ (self):
        super().__init__()
        self.setupUi(self)
        self.callAfterInit()
        self.btnXoaDialog.clicked.connect(self.deletefood)
        self.btnChinhSuaDialog.clicked.connect(self.showEditDialog)
        self.btnAddDialog.clicked.connect(self.showAddDialog)
        self.btnsearch.clicked.connect(self.searchFood)
        self.pushButton_back.clicked.connect(self.ShowMainPage)
        # self.pushButton_micro.clicked.connect(self.searchFoodByVoice)


    def ShowMainPage(self):
          mainPage.show()
          self.close()

    def deletefood(self):
        nameFoodDelete = self.List_cook.currentItem().text()
        self.List_cook.takeItem(self.List_cook.currentRow())
        self.L.delete_food_by_name(nameFoodDelete)
        self.callAfterInit
    def showAddDialog(self):
        add.show()

    def showEditDialog(self):

        if self.List_cook.currentRow() >= 0:
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
    # def searchFoodByVoice(self):
    #     valueSearch = speech_to_text()
    #     dataSearch = self.L.searchfoodbyname(valueSearch) #--> list object
    #     self.List_cook.clear()
    #     for cok in dataSearch:
    #         self.List_cook.addItem(cok.getName())

class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/LoginPage.ui",self) # Load Giao diện từ file .ui
        

        # ====== Kết nối sự kiện ở đây
        self.pushButton_login.clicked.connect(self.checkLogin)
        self.pushButton_createAccount.clicked.connect(self.showSignupPage)
    def showSignupPage(self):
        signupPage.show()  # Hiển thị trang đăng ký
        self.close()       # Ẩn đi trang đăng nhập
    # Hàm kiểm tra đăng nhập
    def checkLogin(self):

       print(ListAcc.checkAccount(Account(self.lineEdit_Fullname.text(), self.lineEdit_Password.text(),)))
       print(self.lineEdit_Fullname.text() , self.lineEdit_Password.text() ) 
       if ListAcc.checkAccount(Account(self.lineEdit_Fullname.text(), self.lineEdit_Password.text(),)) == True:
           mainPage.show()
           self.close()

               

class SigninPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/SigninPage.ui",self) 
        ListAcc = ListAccount()         
              # ====== Kết nối sự kiện ở đây
        self.pushButton_Gologin.clicked.connect(self.showLoginPage)
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

        ListAcc.addAccount(Account(username,password))
        ListAcc.saveAllAccount()
        self.showLoginPage()
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
        self.pushButton_ranking.clicked.connect(self.ShowRanKingPage)
        self.pushButton_add.clicked.connect(self.ShowAddminPage)
        self.pushButton_setting.clicked.connect(self.showSettingPage)

      def showSettingPage(self):
        settingPage.show()
        self.close()
          

      def ShowRanKingPage(self):
        sorTing.show()  
        self.close()
      def ShowAddminPage(self):
        home.show()
        self.close()
class BookThitKho(QMainWindow):
      def __init__(self):
        super().__init__()
        uic.loadUi("ui/book_thit_kho.ui",self) # Load Giao diện từ file .ui
        self.pushButton_back_2.clicked.connect(self.ShowMainPage)

      def ShowMainPage(self):
          sorTing.show()
          self.close()

class RecipeThitKho(QMainWindow,Ui_recipe):
     def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_back_2.clicked.connect(self.ShowMainPage)

     def ShowMainPage(self):
          sorTing.show()
          self.close()
     def loadObject(self,z):
        self.label_2.setText(z.getRecipe())
        
class SettingPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/setting page.ui",self)
        self.pushButton_back.clicked.connect(self.ShowMainPage)
        self.pushButton_logout.clicked.connect(self.showLoginPage)

    def ShowMainPage(self):
          mainPage.show()
          self.close()
    def showLoginPage(self):
        loginPage.show()  # Hiển thị trang đăng nhập
        self.close()    
        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    loginPage = LoginPage() # Tạo đối tượng LoginPage
    sorTing = SorTing()
    signupPage = SigninPage() # Tạo đối tượng SignupPage
    mainPage = MainPage()
    home = HomeMenuDashboard()
    ListAcc = ListAccount()
    bookThitKho = BookThitKho()
    recipeThitkho = RecipeThitKho()
    settingPage = SettingPage()
   
    add = AddDialog()
    edit = EditDialog()


    mainPage.show() # Hiển thị trang đăng nhập

    sys.exit(app.exec())
