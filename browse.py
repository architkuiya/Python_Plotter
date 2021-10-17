from tkinter import *
from tkinter import filedialog
from graphs import *
import pandas as pd

base = Tk()

# Create a widget
base.geometry('800x800')
base.title('PLOTTER')

#WELCOME SIGN
Label(base,text= '-'*50 +'\nW E L C O M E\n'+ '-'*50,font=("Arial", 25),justify='center').grid(row=0,column=0)

# Function for opening the file
def file_opener():
   input = filedialog.askopenfile(initialdir="Files", filetypes=[("text files", "*.csv")])
   if not input:
      return None
   else:
      Label(base, text = 'File imported successfully').grid(row=6, column=0)   
   file_path = input.name
   file_opener.df = pd.read_csv(file_path)

# Browse button
Label(base, text = 'Click here to browse the csv file').grid(row=5, column=0)
x = Button(base, text ='Select a ".csv" file', command = lambda:file_opener())
x.grid(row=5,column=1)

#column1 & column 2 entry
Label(base, text='Add the names of column1 and column2').grid(row=10,column=0)

column1 = Entry(base)
column1.grid(row=11, column=0)
column1.insert(0,'column_1')

column2 = Entry(base)
column2.grid(row=11, column=1)
column2.insert(0,'column_2')
Button(base, text = 'submit').grid(row=11,column=3)

#ADD COMMAND

Button(base, text='pairplot', command= lambda:pair_plot(file_opener.df)).grid(row=12, column = 0)
Button(base, text='bar chart', command= lambda:bar_plot(file_opener.df[column1.get()], file_opener.df[column2.get()])).grid(row=13, column = 0)
Button(base, text='scatter plot', command= lambda:scatter_plot(file_opener.df[column1.get()], file_opener.df[column2.get()])).grid(row=14, column = 0)
Button(base, text='histogram', command= lambda:hist_plot(file_opener.df[column1.get()], file_opener.df[column2.get()])).grid(row=15, column = 0)
Button(base, text='linechart', command= lambda:plot(file_opener.df[column1.get()], file_opener.df[column2.get()])).grid(row=16, column = 0)

base.mainloop()