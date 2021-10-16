from tkinter import *
from tkinter import filedialog
base = Tk()

# Create a canvas
base.geometry('150x150')

# Function for opening the file
def file_opener():
   input = filedialog.askopenfile(initialdir="Files", filetypes=[("text files", "*.csv")])
   if not input:
      return None
   
   file_path = input.name
   print(file_path)

# Button label
x = Button(base, text ='Select a .txt/.csv file', command = lambda:file_opener())
x.pack()
mainloop()