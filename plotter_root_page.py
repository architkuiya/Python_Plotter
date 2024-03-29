from second_window import *

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Plotter(object):
    #opening second window
    def open_sec_win(self):
        self.window = QtWidgets.QMainWindow()
        self.ui2 = Ui_MainWindow()
        self.ui2.setupUi(self.window)
        self.window.show()

    def setupUi(self, Plotter):
        Plotter.setObjectName("Plotter")
        Plotter.resize(871, 589)
        Plotter.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.columnView_2 = QtWidgets.QColumnView(Plotter)
        self.columnView_2.setGeometry(QtCore.QRect(0, 0, 871, 131))
        self.columnView_2.setObjectName("columnView_2")
        self.label = QtWidgets.QLabel(Plotter)
        self.label.setGeometry(QtCore.QRect(80, 20, 701, 81))
        font = QtGui.QFont()
        font.setFamily("dsrom10")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.importing = QtWidgets.QPushButton(Plotter)
        self.importing.setGeometry(QtCore.QRect(300, 390, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.importing.setFont(font)
        self.importing.setStyleSheet("background-color: rgb(192, 28, 40);")
        self.importing.setObjectName("importing")
        self.proceed = QtWidgets.QPushButton(Plotter)
        self.proceed.setGeometry(QtCore.QRect(720, 550, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.proceed.setFont(font)
        self.proceed.setObjectName("proceed")
        self.label_5 = QtWidgets.QLabel(Plotter)
        self.label_5.setGeometry(QtCore.QRect(660, 510, 181, 19))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Plotter)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 781, 241))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Plotter)
        QtCore.QMetaObject.connectSlotsByName(Plotter)

    def retranslateUi(self, Plotter):
        _translate = QtCore.QCoreApplication.translate
        Plotter.setWindowTitle(_translate("Plotter", "Dialog"))
        self.label.setText(_translate("Plotter", "PYTHON PLOTTER"))
        self.importing.setText(_translate("Plotter", "IMPORT CSV FILE"))
        self.proceed.setText(_translate("Plotter", "Proceed"))
        self.label_5.setText(_translate("Plotter", "File Import check"))
        self.label_2.setText(_translate("Plotter", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Hi! Welcome to our BI tool</span></p><p align=\"center\"><span style=\" color:#1a5fb4;\">We are going to help you take </span></p><p align=\"center\"><span style=\" color:#1a5fb4;\">the best business decisions by </span></p><p align=\"center\"><span style=\" color:#1a5fb4;\">analysing your data through </span></p><p align=\"center\"><span style=\" color:#1a5fb4;\">our wide range of charts. </span></p><p align=\"center\"><span style=\" text-decoration: underline;\">Please browse for your .csv file by clicking the button given below.</span></p></body></html>"))