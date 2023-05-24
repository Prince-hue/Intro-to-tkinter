import tkinter as tk
from tkinter import ttk #gives us more options to choose widget from

root = tk.Tk()
roots = ttk.Notebook(root) #widgets that manages a collection of windows/displays

#In order to create different tabs, we create some frames first
tab1 = tk.Frame(roots)
tab2 = tk.Frame(roots)
tab3 = tk.Frame(roots)
#creating tabs or windows
roots.add(tab1, text='Tab 1')
roots.add(tab2, text='Tab 2')
roots.add(tab3, text='Tab 3')
roots.pack(expand=True, fill='both') #expand --enlarges to accomodate space: fill --covers x & y empty spaces
#creating labels
tk.Label(tab1, text='Hello, this is tab number one', width=50, height=25, bg='blue').pack()
tk.Label(tab2, text='Hello, this is tab number two', width=50, height=25, bg='red').pack()
tk.Label(tab3, text='Hello, this is tab number three', bg='yellow').pack()
tk.Label(root, text='This will show regardless of the tab you select', width=50, height=5).pack()

root.mainloop()