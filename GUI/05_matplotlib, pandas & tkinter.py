import tkinter as tk
from tkinter import filedialog

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

root = tk.Tk()

#Build a plot
fig = plt.figure(1)
t = np.arange(0.0, 3.0, 0.01)
s = np.sin(np.pi*t)
plt.plot(t, s)

#the plot is placed on a canvas
canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()

#read csv files
def open_file():
    file = filedialog.askopenfilename(#mode='r', 
                                      filetypes= [('CSV File Only', '.csv')])
    if file is not None:
        data = pd.read_csv(file)
        x = data['GR']
        y = data['DEPTH']
        plt.plot(x, y)
        plt.xlabel('GR')
        plt.ylabel('Depth')
        #plt.draw()
        #plt.canvas.draw()
    else:
        print('nothing')
tk.Button(root,
          text='Open',
          command=open_file).grid(row=2, column=1)
def update():
    fig.canvas.draw()

def _quit():
    root.quit()
    root.destroy()

plot_widget.grid(row=0, column=0)
tk.Button(root, text='Update', command=update).grid(row=1, column=0)

#add a quit button below the update button
tk.Button(root, text='Quit', command=_quit).grid(row=2, column=0)

root.mainloop()

