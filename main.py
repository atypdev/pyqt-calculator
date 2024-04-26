import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5 import QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(292, 371)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -10, 291, 341))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 271, 61))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(11, 92, 63, 34))
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.setEditText(self.pushButton, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(80, 92, 63, 34))
        self.pushButton_9.setDefault(False)
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(lambda: self.setEditText(self.pushButton_9, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(149, 92, 63, 34))
        self.pushButton_10.setDefault(False)
        self.pushButton_10.setFlat(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(lambda: self.setEditText(self.pushButton_10, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(218, 92, 62, 34))
        self.pushButton_12.setDefault(False)
        self.pushButton_12.setFlat(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(lambda: self.setEditText(self.pushButton_12, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(11, 153, 63, 34))
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda: self.setEditText(self.pushButton_5, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 153, 63, 34))
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.setEditText(self.pushButton_2, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(149, 153, 63, 34))
        self.pushButton_7.setDefault(False)
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda: self.setEditText(self.pushButton_7, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(218, 175, 62, 34))
        self.pushButton_8.setDefault(False)
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda: self.setEditText(self.pushButton_8, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(11, 214, 63, 34))
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.setEditText(self.pushButton_3, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(11, 275, 63, 34))
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.setEditText(self.pushButton_4, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(80, 214, 63, 34))
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda: self.setEditText(self.pushButton_6, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(149, 214, 63, 34))
        self.pushButton_11.setDefault(False)
        self.pushButton_11.setFlat(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(lambda: self.setEditText(self.pushButton_11, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(218, 225, 62, 34))
        self.pushButton_13.setDefault(False)
        self.pushButton_13.setFlat(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(lambda: self.setEditText(self.pushButton_13, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(80, 275, 63, 34))
        self.pushButton_14.setDefault(False)
        self.pushButton_14.setFlat(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(lambda: self.setEditText(self.pushButton_14, self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setGeometry(QtCore.QRect(149, 275, 63, 34))
        self.pushButton_15.setDefault(False)
        self.pushButton_15.setFlat(True)
        self.pushButton_15.setObjectName("clear")
        self.pushButton_15.clicked.connect(lambda: self.clear(self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_16 = QtWidgets.QPushButton(self.frame)
        self.pushButton_16.setGeometry(QtCore.QRect(218, 275, 62, 34))
        self.pushButton_16.setDefault(False)
        self.pushButton_16.setObjectName("enter")
        self.pushButton_16.clicked.connect(lambda: self.button_clicked(self.lineEdit))
        self.lineEdit.setFocus()

        self.pushButton_16.setShortcut(QKeySequence("Return"))

        self.pushButton_17 = QtWidgets.QPushButton(self.frame)
        self.pushButton_17.setGeometry(QtCore.QRect(217, 130, 63, 34))
        self.pushButton_17.setDefault(False)
        self.pushButton_17.setFlat(True)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.clicked.connect(lambda: self.setEditText(self.pushButton_17, self.lineEdit))
        self.lineEdit.setFocus()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 292, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "7"))
        self.pushButton_9.setText(_translate("MainWindow", "8"))
        self.pushButton_10.setText(_translate("MainWindow", "9"))
        self.pushButton_12.setText(_translate("MainWindow", " * "))
        self.pushButton_17.setText(_translate("MainWindow", " / "))
        self.pushButton_5.setText(_translate("MainWindow", "4"))
        self.pushButton_2.setText(_translate("MainWindow", "5"))
        self.pushButton_7.setText(_translate("MainWindow", "6"))
        self.pushButton_8.setText(_translate("MainWindow", " - "))
        self.pushButton_3.setText(_translate("MainWindow", "1"))
        self.pushButton_6.setText(_translate("MainWindow", "2"))
        self.pushButton_11.setText(_translate("MainWindow", "3"))
        self.pushButton_13.setText(_translate("MainWindow", " + "))
        self.pushButton_4.setText(_translate("MainWindow", "0"))
        self.pushButton_14.setText(_translate("MainWindow", "."))
        self.pushButton_15.setText(_translate("MainWindow", "Clear"))
        self.pushButton_16.setText(_translate("MainWindow", " = "))

    def setEditText(self, pushButton, lineEdit):
        num = pushButton.text()
        lineEdit.setText(str(self.lineEdit.text()+num))
    def evaluateExp(self, expression):
        try:
            result = eval(expression)
        except (ValueError, SyntaxError, ArithmeticError) as e:
            result = f"Error: {type(e).__name__} - {str(e)}"
        except Exception as e:
            result = f"Unknown Error: {type(e).__name__} - {str(e)}"
        return result
    def clear(self, lineEdit):
        self.lineEdit.setText('')
    def button_clicked(self, ledit):
        exp = ledit.text()
        res = str(self.evaluateExp(exp))
        ledit.setText(res)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("Qt Calculator")
    MainWindow.show()
    sys.exit(app.exec_())