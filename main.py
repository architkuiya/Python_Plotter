from plotter_root_page import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QPushButton, QVBoxLayout, QFileDialog


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog() 
ui = Ui_Plotter()

#importing function
def open_file(self):
        try:
            path = QFileDialog.getOpenFileName(filter='*.csv')          
            if path != ('', ''):
                print(path[0])

                ui.label_5.setText("File imported successfully")
        except: 
            ui.label_5.setText("File not imported")

if __name__ == "__main__":
    
    ui.setupUi(Dialog)
    
    ui.importing.clicked.connect(open_file)
    
    Dialog.show()
    sys.exit(app.exec_())
# importing function open_file
