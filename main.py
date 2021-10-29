from plotter_root_page import *

from second_window import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QPushButton, QVBoxLayout, QFileDialog

#first window creation
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog() 
ui = Ui_Plotter()
ui2 = Ui_MainWindow()

def pair_plt():
    print("DONE")
    colour = ui2.marker_pp.currentText()
    print(colour)
    


#importing csv file 
def open_file(self):
        # try:
            path = QFileDialog.getOpenFileName(filter='*.csv')          
            if path != ('', ''):
                print(path[0])

                #proceed button
                ui.proceed.clicked.connect(ui.open_sec_win)
                
                ui.label_5.setText("File imported successfully")
        # except: 
        #     ui.label_5.setText("File not imported")

if __name__ == "__main__":
    
    ui.setupUi(Dialog)
    MainWindow = QtWidgets.QMainWindow()
    ui2.setupUi(MainWindow)
    print("0000")
    #import button
    ui.importing.clicked.connect(open_file)
    
    print(MainWindow.isActiveWindow())
    print("11111")
    ui2.plot_pp.clicked.connect(pair_plt)
    print("22222")
        
    
    
    
    Dialog.show()
    sys.exit(app.exec_())