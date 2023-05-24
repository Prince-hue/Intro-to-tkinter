#importing tkinter into python
import tkinter as tk

#creating a window
root = tk.Tk()
#resizing a window
root.geometry('500x500')
#adding a title
root.title('BUDGET')
#adding a label
txt = "Running on a budget is as safe as driving within speed limits"
label = tk.Label(root, text=txt, font=('Arial', 12))
label.pack(padx=20, pady=20)
#adding a textbox
textbox = tk.Text(root, height=3, font=('Arial', 14))
textbox.pack(padx=10)
#adding a button
btn = tk.Button(root, text='click me')
btn.pack(padx=10, pady=10)

#grids of buttons
btnframe = tk.Frame(root)
#number of columns
btnframe.columnconfigure(0, weight=4) #coln 1
btnframe.columnconfigure(1, weight=1) #coln 2
btnframe.columnconfigure(2, weight=1) #coln 3
#stacking buttons into grid 
btn1 = tk.Button(btnframe, text = 'Income')
btn1.grid(row=0, column=0)

btn2 = tk.Button(btnframe, text = 'Records')
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(btnframe, text = 'Expenditure')
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(btnframe, text = 'Earnings')
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(btnframe, text = 'Report')
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(btnframe, text = 'Plot')
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

btnframe.pack(fill='x')

#using place instead of pack
btn_p = tk.Button(root, text='Preview')
btn_p.place(x=400, y=400, height=100, width=100)



root.mainloop()
