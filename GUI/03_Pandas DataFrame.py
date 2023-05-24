import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pandas as pd

root = tk.Tk()
root.title('DataFrame Work')
root.geometry('600x500')

#Creating a font Style variable
fontStyle=('times', 18, 'bold')

#label
intro = tk.Label(root, text='DataFrame', width=30, font=fontStyle)
intro.grid(row=0, column=1)

#we create a Button and add a command to upload a file but the command hasn't yet been decleared
btn = tk.Button(root, text='Browse File', width=20, 
                command=lambda:upload_file())
btn.grid(row=1, column=1)

#textbox
txtbox = tk.Text(root, height=9, width=45, bg='yellow')
txtbox.grid(row=2, column=1, pady=10)

#declearing the upload file command
def upload_file():
    #we use file type to define the file we need
    file=filedialog.askopenfilename(
        filetypes=[('Comma Separated Values File','.csv')])
    #
    #creating a dataFrame
    df = pd.read_csv(file)
    txtbox.insert(tk.END, df.head(40))
   

root.mainloop()