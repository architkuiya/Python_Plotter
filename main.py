from plotter_root_page import *

# from second_window import *
import pandas as pd
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QFileDialog
from PyQt5 import QtWidgets




#first window creation
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Plotter()




#importing csv file 
def open_file(self):
        # try:
            path = QFileDialog.getOpenFileName(filter='*.csv')          
            if path != ('', ''):
                print(path[0])

                open_file.data = pd.read_csv(path[0])

                #proceed button
                ui.proceed.clicked.connect(ui.open_sec_win)
                
                ui.label_5.setText("File imported successfully")
        # except: 
        #     ui.label_5.setText("File not imported")

if __name__ == "__main__":
    
    ui.setupUi(Dialog)
    
    ui.importing.clicked.connect(open_file)

    Dialog.show()
    sys.exit(app.exec_())