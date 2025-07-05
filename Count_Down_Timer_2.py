from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(421, 208)
        SecondWindow.setStyleSheet("background-color: #E8D4C6")
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.countdown_label = QtWidgets.QLabel(self.centralwidget)
        self.countdown_label.setGeometry(QtCore.QRect(80, 20, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.countdown_label.setFont(font)
        self.countdown_label.setAlignment(QtCore.Qt.AlignCenter)
        self.countdown_label.setObjectName("countdown_label")
        self.PR_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.PR_pushButton.setGeometry(QtCore.QRect(190, 120, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PR_pushButton.setFont(font)
        self.PR_pushButton.setStyleSheet("QPushButton {\n"
"    background: #ADADAD;\n"
"    border: 2px solid;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #D6D6D6;\n"
"    border: 2px solid #5C5C5C;\n"
"}")
        self.PR_pushButton.setObjectName("PR_pushButton")
        self.reset_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.reset_pushButton.setGeometry(QtCore.QRect(30, 120, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.reset_pushButton.setFont(font)
        self.reset_pushButton.setStyleSheet("QPushButton {\n"
"    background: #ADADAD;\n"
"    border: 2px solid;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #D6D6D6;\n"
"    border: 2px solid #5C5C5C;\n"
"}")
        self.reset_pushButton.setObjectName("reset_pushButton")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 421, 21))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MainWindow"))
        self.countdown_label.setText(_translate("SecondWindow", "00:00:00"))
        self.PR_pushButton.setText(_translate("SecondWindow", "Pause/Resume"))
        self.reset_pushButton.setText(_translate("SecondWindow", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())
