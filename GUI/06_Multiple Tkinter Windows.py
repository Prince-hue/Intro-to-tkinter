import tkinter as tk


root = tk.Tk()
root.geometry('500x500')
root.title('Window one')

def open():
    #top level is used to display a new window
    root2 = tk.Toplevel()
    root2.title('Second Window')
    root2.geometry('200x200')

    label = tk.Label(root2, text="This is our second window").pack(pady=10)
    btnclose = tk.Button(root2, text='Exit Window', command=root2.destroy).pack(pady=10)

btn = tk.Button(root, text='Open Window 2', command=open).pack(pady=10)

root.mainloop()