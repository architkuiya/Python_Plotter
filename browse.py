from tkinter import *
from tkinter import filedialog
from tkinter.font import Font
from graphs import *
import pandas as pd

base = Tk()

# Create a widget
base.geometry('550x600')
base.title('PLOTTER')

#WELCOME SIGN
Label(base,text= '-'*50 +'\nW E L C O M E\n'+ '-'*50,font=("Arial", 25),justify='center',bg='black',fg='white').grid(row=0,column=0,columnspan=6)

# Function for opening the file
def file_opener():
   input = filedialog.askopenfile(initialdir="Files", filetypes=[("text files", "*.csv")])
   if not input:
      return None
   else:
      Label(base, text = 'File imported successfully\n'+'-'*50).grid(row=10, column=0)   
   file_path = input.name
   file_opener.df = pd.read_csv(file_path)

# Browse button
Label(base, text = 'Click here to browse the csv file').grid(row=9, column=0)
x = Button(base, text ='Select a ".csv" file', command = lambda:file_opener())
x.grid(row=9,column=1)

#column1 & column 2 entry
Label(base, text='Add the names of column1 and column2').grid(row=14,column=0,columnspan=4,pady=20,padx=50)

column1 = Entry(base)
column1.grid(row=15, column=0)

column2 = Entry(base)
column2.grid(row=15, column=1)


#ADD COMMAND
Button(base, text='pairplot', command= lambda:pair_plot(file_opener.df),justify='center').grid(row=13, column = 0,pady=20,padx=200,columnspan=4)
Button(base, text='bar chart', command= lambda:bar_plot(file_opener.df[column1.get()], file_opener.df[column2.get()])).grid(row=17, column = 0,pady=20,padx=20)
Button(base, text='scatter plot', command= lambda:scatter_plot(file_opener.df[column1.get()], file_opener.df[column2.get()])).grid(row=17, column = 1,pady=20,padx=20)
Button(base, text='histogram', command= lambda:hist_plot(file_opener.df[column1.get()], file_opener.df[column2.get()])).grid(row=18, column = 0,pady=20,padx=20)
Button(base, text='linechart', command= lambda:plot(file_opener.df[column1.get()], file_opener.df[column2.get()])).grid(row=18, column = 1,pady=20,padx=20)
base.mainloop()