# Form implementation generated from reading ui file 'ui/MainPage.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(811, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 811, 571))
        self.widget.setStyleSheet("background-color:rgb(33, 35, 40)\n"
"")
        self.widget.setObjectName("widget")
        self.label_7 = QtWidgets.QLabel(parent=self.widget)
        self.label_7.setGeometry(QtCore.QRect(300, 30, 91, 81))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("D:/download/chef.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.widget_2.setGeometry(QtCore.QRect(90, 130, 671, 351))
        self.widget_2.setStyleSheet("border-radius:20px;background-color: rgb(57, 60, 68)")
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QtWidgets.QWidget(parent=self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(30, 10, 191, 271))
        self.widget_3.setStyleSheet("background-color:rgb(31, 31, 31)")
        self.widget_3.setObjectName("widget_3")
        self.label_3 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 171, 101))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("ui\\../../../Pictures/Screenshots/Screenshot 2024-06-30 221921.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(40, 120, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_5.setGeometry(QtCore.QRect(50, 150, 21, 21))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("D:/download/star.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(10, 150, 31, 20))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("D:/download/like.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(70, 150, 21, 21))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("D:/download/star.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_9.setGeometry(QtCore.QRect(90, 150, 21, 21))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("D:/download/star.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_10.setGeometry(QtCore.QRect(110, 150, 21, 21))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("D:/download/star.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_11.setGeometry(QtCore.QRect(130, 150, 21, 21))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("D:/download/star.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_12.setGeometry(QtCore.QRect(10, 190, 31, 31))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("D:/download/comment.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 190, 111, 22))
        self.lineEdit_2.setStyleSheet("background-color: rgb(57, 60, 68)")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_recipe_Thitkho = QtWidgets.QPushButton(parent=self.widget_3)
        self.pushButton_recipe_Thitkho.setGeometry(QtCore.QRect(20, 230, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.pushButton_recipe_Thitkho.setFont(font)
        self.pushButton_recipe_Thitkho.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/download/recipe-book.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_recipe_Thitkho.setIcon(icon)
        self.pushButton_recipe_Thitkho.setIconSize(QtCore.QSize(30, 60))
        self.pushButton_recipe_Thitkho.setObjectName("pushButton_recipe_Thitkho")
        self.pushButton_book_thitkho = QtWidgets.QPushButton(parent=self.widget_3)
        self.pushButton_book_thitkho.setGeometry(QtCore.QRect(80, 220, 61, 61))
        self.pushButton_book_thitkho.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:/download/book.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_book_thitkho.setIcon(icon1)
        self.pushButton_book_thitkho.setIconSize(QtCore.QSize(30, 70))
        self.pushButton_book_thitkho.setObjectName("pushButton_book_thitkho")
        self.widget_4 = QtWidgets.QWidget(parent=self.widget_2)
        self.widget_4.setGeometry(QtCore.QRect(250, 10, 191, 271))
        self.widget_4.setStyleSheet("background-color:rgb(31, 31, 31)")
        self.widget_4.setObjectName("widget_4")
        self.label_13 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_13.setGeometry(QtCore.QRect(10, 10, 171, 101))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("ui\\../../../Pictures/Screenshots/Screenshot 2024-06-30 223013.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_14.setGeometry(QtCore.QRect(30, 120, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_15.setGeometry(QtCore.QRect(50, 150, 21, 21))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("D:/download/star.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_16.setGeometry(QtCore.QRect(10, 150, 31, 20))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("D:/download/like.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_17.setGeometry(QtCore.QRect(70, 150, 21, 21))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("D:/download/star.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_18.setGeometry(QtCore.QRect(90, 150, 21, 21))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("D:/download/star.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_19.setGeometry(QtCore.QRect(110, 150, 21, 21))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("D:/download/star.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.label_21 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_21.setGeometry(QtCore.QRect(10, 190, 31, 31))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("D:/download/comment.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.widget_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(50, 190, 111, 22))
        self.lineEdit_4.setStyleSheet("background-color: rgb(57, 60, 68)")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_recipe_gachien = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_recipe_gachien.setGeometry(QtCore.QRect(30, 230, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.pushButton_recipe_gachien.setFont(font)
        self.pushButton_recipe_gachien.setText("")
        self.pushButton_recipe_gachien.setIcon(icon)
        self.pushButton_recipe_gachien.setIconSize(QtCore.QSize(30, 60))
        self.pushButton_recipe_gachien.setObjectName("pushButton_recipe_gachien")
        self.pushButton_book_gachien = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_book_gachien.setGeometry(QtCore.QRect(90, 220, 61, 61))
        self.pushButton_book_gachien.setText("")
        self.pushButton_book_gachien.setIcon(icon1)
        self.pushButton_book_gachien.setIconSize(QtCore.QSize(30, 70))
        self.pushButton_book_gachien.setObjectName("pushButton_book_gachien")
        self.listWidget = QtWidgets.QListWidget(parent=self.widget_4)
        self.listWidget.setGeometry(QtCore.QRect(-320, -110, 781, 551))
        self.listWidget.setObjectName("listWidget")
        self.widget_7 = QtWidgets.QWidget(parent=self.widget_4)
        self.widget_7.setGeometry(QtCore.QRect(0, 0, 191, 271))
        self.widget_7.setStyleSheet("background-color:rgb(31, 31, 31)")
        self.widget_7.setObjectName("widget_7")
        self.label_56 = QtWidgets.QLabel(parent=self.widget_7)
        self.label_56.setGeometry(QtCore.QRect(10, 10, 171, 101))
        self.label_56.setText("")
        self.label_56.setPixmap(QtGui.QPixmap("ui\\../../../Pictures/Screenshots/Screenshot 2024-06-30 223013.png"))
        self.label_56.setScaledContents(True)
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(parent=self.widget_7)
        self.label_57.setGeometry(QtCore.QRect(30, 120, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_57.setFont(font)
        self.label_57.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(parent=self.widget_7)
        self.label_58.setGeometry(QtCore.QRect(50, 150, 21, 21))
        self.label_58.setText("")
        self.label_58.setPixmap(QtGui.QPixmap("D:/download/star.png"))
        self.label_58.setScaledContents(True)
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(parent=self.widget_7)
        self.label_59.setGeometry(QtCore.QRect(10, 150, 31, 20))
        self.label_59.setText("")
        self.label_59.setPixmap(QtGui.QPixmap("D:/download/like.png"))
        self.label_59.setScaledContents(True)
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(parent=self.widget_7)
        self.label_60.setGeometry(QtCore.QRect(70, 150, 21, 21))
        self.label_60.setText("")
        self.label_60.setPixmap(QtGui.QPixmap("D:/download/star.png"))
        self.label_60.setScaledContents(True)
        self.label_60.setObjectName("label_60")
        self.label_61 = QtWidgets.QLabel(parent=self.widget_7)
        self.label_61.setGeometry(QtCore.QRect(90, 150, 21, 21))
        self.label_61.setText("")
        self.label_61.setPixmap(QtGui.QPixmap("D:/download/star.png"))
        self.label_61.setScaledContents(True)
        self.label_61.setObjectName("label_61")
        self.label_62 = QtWidgets.QLabel(parent=self.widget_7)
        self.label_62.setGeometry(QtCore.QRect(110, 150, 21, 21))
        self.label_62.setText("")
        self.label_62.setPixmap(QtGui.QPixmap("D:/download/star.png"))
        self.label_62.setScaledContents(True)
        self.label_62.setObjectName("label_62")
        self.label_63 = QtWidgets.QLabel(parent=self.widget_7)
        self.label_63.setGeometry(QtCore.QRect(10, 190, 31, 31))
        self.label_63.setText("")
        self.label_63.setPixmap(QtGui.QPixmap("D:/download/comment.png"))
        self.label_63.setScaledContents(True)
        self.label_63.setObjectName("label_63")
        self.lineEdit_10 = QtWidgets.QLineEdit(parent=self.widget_7)
        self.lineEdit_10.setGeometry(QtCore.QRect(50, 190, 111, 22))
        self.lineEdit_10.setStyleSheet("background-color: rgb(57, 60, 68)")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pushButton_recipe_gachien_5 = QtWidgets.QPushButton(parent=self.widget_7)
        self.pushButton_recipe_gachien_5.setGeometry(QtCore.QRect(30, 230, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.pushButton_recipe_gachien_5.setFont(font)
        self.pushButton_recipe_gachien_5.setText("")
        self.pushButton_recipe_gachien_5.setIcon(icon)
        self.pushButton_recipe_gachien_5.setIconSize(QtCore.QSize(30, 60))
        self.pushButton_recipe_gachien_5.setObjectName("pushButton_recipe_gachien_5")
        self.pushButton_book_gachien_5 = QtWidgets.QPushButton(parent=self.widget_7)
        self.pushButton_book_gachien_5.setGeometry(QtCore.QRect(90, 220, 61, 61))
        self.pushButton_book_gachien_5.setText("")
        self.pushButton_book_gachien_5.setIcon(icon1)
        self.pushButton_book_gachien_5.setIconSize(QtCore.QSize(30, 70))
        self.pushButton_book_gachien_5.setObjectName("pushButton_book_gachien_5")
        self.widget_5 = QtWidgets.QWidget(parent=self.widget_2)
        self.widget_5.setGeometry(QtCore.QRect(470, 10, 191, 271))
        self.widget_5.setStyleSheet("background-color:rgb(31, 31, 31)")
        self.widget_5.setObjectName("widget_5")
        self.label_20 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_20.setGeometry(QtCore.QRect(10, 10, 171, 101))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("ui\\../../../Pictures/Screenshots/Screenshot 2024-06-30 223153.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.label_22 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_22.setGeometry(QtCore.QRect(40, 120, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_23.setGeometry(QtCore.QRect(50, 150, 21, 21))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("D:/download/star.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_24.setGeometry(QtCore.QRect(10, 150, 31, 20))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("D:/download/like.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_25.setGeometry(QtCore.QRect(70, 150, 21, 21))
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("D:/download/star.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_26.setGeometry(QtCore.QRect(90, 150, 21, 21))
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap("D:/download/star.png"))
        self.label_26.setScaledContents(True)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_27.setGeometry(QtCore.QRect(110, 150, 21, 21))
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("D:/download/star.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_28.setGeometry(QtCore.QRect(10, 190, 31, 31))
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap("D:/download/comment.png"))
        self.label_28.setScaledContents(True)
        self.label_28.setObjectName("label_28")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.widget_5)
        self.lineEdit_5.setGeometry(QtCore.QRect(50, 190, 111, 22))
        self.lineEdit_5.setStyleSheet("background-color: rgb(57, 60, 68)")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_29 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_29.setGeometry(QtCore.QRect(130, 150, 21, 21))
        self.label_29.setText("")
        self.label_29.setPixmap(QtGui.QPixmap("D:/download/star.png"))
        self.label_29.setScaledContents(True)
        self.label_29.setObjectName("label_29")
        self.pushButton_recipe_canhchua = QtWidgets.QPushButton(parent=self.widget_5)
        self.pushButton_recipe_canhchua.setGeometry(QtCore.QRect(30, 230, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.pushButton_recipe_canhchua.setFont(font)
        self.pushButton_recipe_canhchua.setText("")
        self.pushButton_recipe_canhchua.setIcon(icon)
        self.pushButton_recipe_canhchua.setIconSize(QtCore.QSize(30, 60))
        self.pushButton_recipe_canhchua.setObjectName("pushButton_recipe_canhchua")
        self.pushButton_book_thitkho_3 = QtWidgets.QPushButton(parent=self.widget_5)
        self.pushButton_book_thitkho_3.setGeometry(QtCore.QRect(90, 220, 61, 61))
        self.pushButton_book_thitkho_3.setText("")
        self.pushButton_book_thitkho_3.setIcon(icon1)
        self.pushButton_book_thitkho_3.setIconSize(QtCore.QSize(30, 70))
        self.pushButton_book_thitkho_3.setObjectName("pushButton_book_thitkho_3")
        self.label_30 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_30.setGeometry(QtCore.QRect(40, 290, 41, 31))
        self.label_30.setText("")
        self.label_30.setPixmap(QtGui.QPixmap("D:/download/search.png"))
        self.label_30.setScaledContents(True)
        self.label_30.setObjectName("label_30")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.widget_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(90, 290, 561, 41))
        self.lineEdit_6.setStyleSheet("border-radius:10px;background-color:rgb(31, 31, 31)\n"
"")
        self.lineEdit_6.setPlaceholderText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_31 = QtWidgets.QLabel(parent=self.widget)
        self.label_31.setGeometry(QtCore.QRect(390, 20, 131, 111))
        self.label_31.setText("")
        self.label_31.setPixmap(QtGui.QPixmap("D:/download/Screenshot_2024-06-30_223704-removebg-preview.png"))
        self.label_31.setScaledContents(True)
        self.label_31.setObjectName("label_31")
        self.widget_6 = QtWidgets.QWidget(parent=self.widget)
        self.widget_6.setGeometry(QtCore.QRect(0, 10, 71, 551))
        self.widget_6.setStyleSheet("border-radius:20px;background-color: rgb(57, 60, 68)")
        self.widget_6.setObjectName("widget_6")
        self.label = QtWidgets.QLabel(parent=self.widget_6)
        self.label.setGeometry(QtCore.QRect(10, 20, 51, 41))
        self.label.setStyleSheet("background-color: rgb(57, 60, 68)")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:/download/menu.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.widget_6)
        self.label_2.setGeometry(QtCore.QRect(10, 500, 51, 41))
        self.label_2.setStyleSheet("background-color: rgb(57, 60, 68)")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("D:/download/settings.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_add = QtWidgets.QPushButton(parent=self.widget_6)
        self.pushButton_add.setGeometry(QtCore.QRect(0, 420, 71, 61))
        self.pushButton_add.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:/download/plus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_add.setIcon(icon2)
        self.pushButton_add.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_add.setObjectName("pushButton_add")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Thịt kho hột vịt"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Leave your review"))
        self.label_14.setText(_translate("MainWindow", "Gà chiên nước mắm"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Leave your review"))
        self.label_57.setText(_translate("MainWindow", "Gà chiên nước mắm"))
        self.lineEdit_10.setPlaceholderText(_translate("MainWindow", "Leave your review"))
        self.label_22.setText(_translate("MainWindow", "Canh chua cá hú"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Leave your review"))