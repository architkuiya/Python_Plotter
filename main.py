from plotter_root_page import *

from second_window import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QPushButton, QVBoxLayout, QFileDialog


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog() 
ui = Ui_Plotter()
ui2 = Ui_MainWindow()

def line_plt():
    print("DONE")
    colour = ui2.colors_lp.currentText()
    print(colour)
    


#importing csv file 
def open_file(self):
        try:
            path = QFileDialog.getOpenFileName(filter='*.csv')          
            if path != ('', ''):
                print(path[0])
                ui.pushButton.clicked.connect(ui.open_sec_win)
                ui.label_5.setText("File imported successfully")
        except: 
            ui.label_5.setText("File not imported")

if __name__ == "__main__":
    
    ui.setupUi(Dialog)
    
    
    #import button
    ui.importing.clicked.connect(open_file)
    
    Dialog.show()
    sys.exit(app.exec_())

    x = "jaskirat"
    ui2.pushButton_2.clicked.connect(lambda x: print(x))
