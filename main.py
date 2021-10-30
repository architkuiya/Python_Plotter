from plotter_root_page import *
import os
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
                # print(path[0])

                f = open("temp/dataframe_path.txt", 'w')
                with open('temp/dataframe_path.txt', 'w') as f:
                    f.write(path[0])
                    f.close()


                #proceed button
                ui.proceed.clicked.connect(ui.open_sec_win)
                
                ui.label_5.setText("File imported successfully")
        # except: 
        #     ui.label_5.setText("File not imported")

if __name__ == "__main__":

    os.remove("temp/dataframe_path.txt")
    
    ui.setupUi(Dialog)
    
    ui.importing.clicked.connect(open_file)

    Dialog.show()
    sys.exit(app.exec_())